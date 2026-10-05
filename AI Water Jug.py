import tkinter as tk
from tkinter import messagebox
from collections import deque


# ============================================================
# AQUAMIND NEXUS
# AI WATER JUG GAME
# HUMAN VS AI
# STATE-SPACE SEARCH USING BFS
# ============================================================


class AquaMindGame:

    def __init__(self, root):

        self.root = root

        # ====================================================
        # WINDOW
        # ====================================================

        self.root.title(
            "AquaMind Nexus | AI Water Jug Challenge"
        )

        self.root.geometry("1400x850")
        self.root.minsize(1200, 760)

        self.root.configure(
            bg="#070B18"
        )

        # ====================================================
        # COLOR PALETTE
        # ====================================================

        self.BG = "#070B18"
        self.BG2 = "#0B1024"

        self.PANEL = "#10172D"
        self.PANEL2 = "#151D38"

        self.CYAN = "#00E5FF"
        self.BLUE = "#3B82F6"
        self.PURPLE = "#A855F7"
        self.PINK = "#EC4899"

        self.GREEN = "#22C55E"
        self.YELLOW = "#FACC15"
        self.RED = "#F43F5E"

        self.WHITE = "#F8FAFC"
        self.LIGHT = "#CBD5E1"
        self.GRAY = "#64748B"

        self.WATER = "#00C8FF"
        self.WATER_LIGHT = "#67E8F9"

        # ====================================================
        # GAME VARIABLES
        # ====================================================

        self.capacity_a = tk.IntVar(value=4)
        self.capacity_b = tk.IntVar(value=3)
        self.target = tk.IntVar(value=2)

        # HUMAN

        self.user_a = 0
        self.user_b = 0
        self.user_moves = 0

        # AI

        self.ai_a = 0
        self.ai_b = 0
        self.ai_moves = 0

        self.ai_solution = []
        self.ai_step = 0
        self.ai_states_explored = 0

        # GAME

        self.game_finished = False
        self.ai_running = False

        self.user_score = 0
        self.ai_score = 0

        # ====================================================
        # BUILD
        # ====================================================

        self.create_sidebar()
        self.create_dashboard()

        self.update_everything()

    # ========================================================
    # SIDEBAR
    # ========================================================

    def create_sidebar(self):

        self.sidebar = tk.Frame(
            self.root,
            bg=self.BG2,
            width=270
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(False)

        # ----------------------------------------------------
        # LOGO
        # ----------------------------------------------------

        logo = tk.Frame(
            self.sidebar,
            bg=self.BG2
        )

        logo.pack(
            fill="x",
            padx=20,
            pady=25
        )

        tk.Label(
            logo,
            text="💧",
            font=("Segoe UI Emoji", 34),
            bg=self.BG2,
            fg=self.CYAN
        ).pack(
            side="left"
        )

        logo_text = tk.Frame(
            logo,
            bg=self.BG2
        )

        logo_text.pack(
            side="left",
            padx=8
        )

        tk.Label(
            logo_text,
            text="AQUAMIND",
            font=("Segoe UI", 18, "bold"),
            bg=self.BG2,
            fg=self.WHITE
        ).pack(
            anchor="w"
        )

        tk.Label(
            logo_text,
            text="N E X U S",
            font=("Segoe UI", 8, "bold"),
            bg=self.BG2,
            fg=self.CYAN
        ).pack(
            anchor="w"
        )

        # ----------------------------------------------------
        # NEON LINE
        # ----------------------------------------------------

        tk.Frame(
            self.sidebar,
            bg=self.CYAN,
            height=2
        ).pack(
            fill="x",
            padx=20
        )

        # ----------------------------------------------------
        # MENU
        # ----------------------------------------------------

        tk.Label(
            self.sidebar,
            text="CONTROL CENTER",
            font=("Segoe UI", 8, "bold"),
            bg=self.BG2,
            fg=self.GRAY
        ).pack(
            anchor="w",
            padx=25,
            pady=(25, 10)
        )

        self.sidebar_button(
            "◈   AI WATER JUG",
            True
        )

        self.sidebar_button(
            "◉   STATE SPACE"
        )

        self.sidebar_button(
            "◆   BFS SEARCH"
        )

        # ----------------------------------------------------
        # MODE CARD
        # ----------------------------------------------------

        mode = tk.Frame(
            self.sidebar,
            bg=self.PANEL,
            highlightbackground="#263354",
            highlightthickness=1
        )

        mode.pack(
            fill="x",
            padx=15,
            pady=20
        )

        tk.Label(
            mode,
            text="GAME MODE",
            font=("Segoe UI", 8, "bold"),
            bg=self.PANEL,
            fg=self.GRAY
        ).pack(
            anchor="w",
            padx=15,
            pady=(15, 5)
        )

        tk.Label(
            mode,
            text="👤 HUMAN",
            font=("Segoe UI", 11, "bold"),
            bg=self.PANEL,
            fg=self.CYAN
        ).pack(
            pady=2
        )

        tk.Label(
            mode,
            text="        VS",
            font=("Segoe UI", 8, "bold"),
            bg=self.PANEL,
            fg=self.GRAY
        ).pack()

        tk.Label(
            mode,
            text="🤖 AI",
            font=("Segoe UI", 11, "bold"),
            bg=self.PANEL,
            fg=self.PINK
        ).pack(
            pady=(2, 15)
        )

        # ----------------------------------------------------
        # ALGORITHM
        # ----------------------------------------------------

        algorithm = tk.Frame(
            self.sidebar,
            bg="#121C36",
            highlightbackground="#253557",
            highlightthickness=1
        )

        algorithm.pack(
            fill="x",
            padx=15,
            pady=5
        )

        tk.Label(
            algorithm,
            text="POWERED BY",
            font=("Segoe UI", 8, "bold"),
            bg="#121C36",
            fg=self.GRAY
        ).pack(
            pady=(15, 3)
        )

        tk.Label(
            algorithm,
            text="BREADTH-FIRST",
            font=("Segoe UI", 12, "bold"),
            bg="#121C36",
            fg=self.PURPLE
        ).pack()

        tk.Label(
            algorithm,
            text="SEARCH",
            font=("Segoe UI", 12, "bold"),
            bg="#121C36",
            fg=self.PURPLE
        ).pack()

        tk.Label(
            algorithm,
            text="STATE-SPACE AI",
            font=("Segoe UI", 8, "bold"),
            bg="#121C36",
            fg=self.GRAY
        ).pack(
            pady=(2, 15)
        )

        # ----------------------------------------------------
        # FOOTER
        # ----------------------------------------------------

        footer = tk.Frame(
            self.sidebar,
            bg=self.BG2
        )

        footer.pack(
            side="bottom",
            pady=20
        )

        tk.Label(
            footer,
            text="AI PROJECT",
            font=("Segoe UI", 8, "bold"),
            bg=self.BG2,
            fg=self.CYAN
        ).pack()

        tk.Label(
            footer,
            text="STATE-SPACE SEARCH LAB",
            font=("Segoe UI", 7),
            bg=self.BG2,
            fg=self.GRAY
        ).pack()

    # ========================================================
    # SIDEBAR BUTTON
    # ========================================================

    def sidebar_button(
        self,
        text,
        active=False
    ):

        bg = "#16254A" if active else self.BG2
        fg = self.CYAN if active else self.GRAY

        button = tk.Frame(
            self.sidebar,
            bg=bg
        )

        button.pack(
            fill="x",
            padx=15,
            pady=3
        )

        tk.Label(
            button,
            text=text,
            font=("Segoe UI", 9, "bold"),
            bg=bg,
            fg=fg
        ).pack(
            anchor="w",
            padx=15,
            pady=10
        )

    # ========================================================
    # MAIN DASHBOARD
    # ========================================================

    def create_dashboard(self):

        self.main = tk.Frame(
            self.root,
            bg=self.BG
        )

        self.main.pack(
            side="right",
            fill="both",
            expand=True
        )

        # ====================================================
        # HEADER
        # ====================================================

        header = tk.Frame(
            self.main,
            bg=self.BG
        )

        header.pack(
            fill="x",
            padx=28,
            pady=(22, 12)
        )

        title_frame = tk.Frame(
            header,
            bg=self.BG
        )

        title_frame.pack(
            side="left"
        )

        tk.Label(
            title_frame,
            text="WATER JUG",
            font=("Segoe UI", 27, "bold"),
            bg=self.BG,
            fg=self.WHITE
        ).pack(
            side="left"
        )

        tk.Label(
            title_frame,
            text="  AI CHALLENGE",
            font=("Segoe UI", 27, "bold"),
            bg=self.BG,
            fg=self.CYAN
        ).pack(
            side="left"
        )

        tk.Label(
            self.main,
            text="Human intelligence meets state-space search",
            font=("Segoe UI", 9),
            bg=self.BG,
            fg=self.GRAY
        ).place(
            x=28,
            y=63
        )

        # Status

        status = tk.Frame(
            header,
            bg="#102A27",
            highlightbackground="#1E5149",
            highlightthickness=1
        )

        status.pack(
            side="right"
        )

        self.status_light = tk.Label(
            status,
            text="●",
            font=("Segoe UI", 12),
            bg="#102A27",
            fg=self.GREEN
        )

        self.status_light.pack(
            side="left",
            padx=(10, 5),
            pady=6
        )

        self.status_label = tk.Label(
            status,
            text="SYSTEM READY",
            font=("Segoe UI", 8, "bold"),
            bg="#102A27",
            fg=self.GREEN
        )

        self.status_label.pack(
            side="left",
            padx=(0, 12)
        )

        # ====================================================
        # TOP STATISTICS
        # ====================================================

        stats = tk.Frame(
            self.main,
            bg=self.BG
        )

        stats.pack(
            fill="x",
            padx=25,
            pady=5
        )

        self.create_stat_card(
            stats,
            "👤 YOUR MOVES",
            "0",
            self.CYAN,
            "user_stat"
        )

        self.create_stat_card(
            stats,
            "🤖 AI SHORTEST",
            "0",
            self.PINK,
            "ai_stat"
        )

        self.create_stat_card(
            stats,
            "🔎 STATES EXPLORED",
            "0",
            self.PURPLE,
            "state_stat"
        )

        self.create_stat_card(
            stats,
            "🎯 TARGET",
            "2 L",
            self.YELLOW,
            "target_stat"
        )

        # ====================================================
        # GAME AREA
        # ====================================================

        game_area = tk.Frame(
            self.main,
            bg=self.BG
        )

        game_area.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=15
        )

        # Left side

        left = tk.Frame(
            game_area,
            bg=self.BG
        )

        left.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 8)
        )

        # Right side

        right = tk.Frame(
            game_area,
            bg=self.BG,
            width=365
        )

        right.pack(
            side="right",
            fill="y",
            padx=(8, 0)
        )

        right.pack_propagate(False)

        self.create_arena(left)

        self.create_solution(left)

        self.create_control_panel(right)

        self.create_ai_panel(right)

    # ========================================================
    # STAT CARD
    # ========================================================

    def create_stat_card(
        self,
        parent,
        title,
        value,
        color,
        name
    ):

        card = tk.Frame(
            parent,
            bg=self.PANEL,
            height=70,
            highlightbackground="#1C2945",
            highlightthickness=1
        )

        card.pack(
            side="left",
            fill="x",
            expand=True,
            padx=4
        )

        card.pack_propagate(False)

        tk.Frame(
            card,
            bg=color,
            width=4
        ).pack(
            side="left",
            fill="y"
        )

        content = tk.Frame(
            card,
            bg=self.PANEL
        )

        content.pack(
            fill="both",
            expand=True,
            padx=12
        )

        tk.Label(
            content,
            text=title,
            font=("Segoe UI", 7, "bold"),
            bg=self.PANEL,
            fg=self.GRAY
        ).pack(
            anchor="w",
            pady=(8, 0)
        )

        value_label = tk.Label(
            content,
            text=value,
            font=("Segoe UI", 17, "bold"),
            bg=self.PANEL,
            fg=color
        )

        value_label.pack(
            anchor="w"
        )

        setattr(
            self,
            name,
            value_label
        )

    # ========================================================
    # ARENA
    # ========================================================

    def create_arena(self, parent):

        arena = tk.Frame(
            parent,
            bg=self.PANEL,
            highlightbackground="#27365A",
            highlightthickness=1
        )

        arena.pack(
            fill="x"
        )

        # Header

        arena_header = tk.Frame(
            arena,
            bg=self.PANEL
        )

        arena_header.pack(
            fill="x",
            padx=20,
            pady=(15, 5)
        )

        tk.Label(
            arena_header,
            text="⚔  HUMAN ARENA",
            font=("Segoe UI", 11, "bold"),
            bg=self.PANEL,
            fg=self.CYAN
        ).pack(
            side="left"
        )

        self.player_state = tk.Label(
            arena_header,
            text="STATE  (0, 0)",
            font=("Consolas", 9, "bold"),
            bg=self.PANEL,
            fg=self.LIGHT
        )

        self.player_state.pack(
            side="right"
        )

        # Canvas

        self.arena_canvas = tk.Canvas(
            arena,
            bg=self.PANEL,
            height=220,
            highlightthickness=0
        )

        self.arena_canvas.pack(
            fill="x",
            padx=15
        )

        self.arena_canvas.bind(
            "<Configure>",
            lambda e: self.draw_arena()
        )

        # Target badge

        self.target_badge = tk.Label(
            arena,
            text="🎯 TARGET: 2 LITRES",
            font=("Segoe UI", 9, "bold"),
            bg="#352B10",
            fg=self.YELLOW
        )

        self.target_badge.pack(
            pady=5
        )

        # Controls

        controls = tk.Frame(
            arena,
            bg=self.PANEL
        )

        controls.pack(
            fill="x",
            padx=15,
            pady=(5, 15)
        )

        self.game_button(
            controls,
            "💧 FILL A",
            self.fill_a,
            self.CYAN
        )

        self.game_button(
            controls,
            "💧 FILL B",
            self.fill_b,
            self.BLUE
        )

        self.game_button(
            controls,
            "✕ EMPTY A",
            self.empty_a,
            self.PINK
        )

        self.game_button(
            controls,
            "✕ EMPTY B",
            self.empty_b,
            self.PURPLE
        )

        self.game_button(
            controls,
            "A  ➜  B",
            self.pour_a_b,
            self.GREEN
        )

        self.game_button(
            controls,
            "B  ➜  A",
            self.pour_b_a,
            self.YELLOW
        )

    # ========================================================
    # GAME BUTTON
    # ========================================================

    def game_button(
        self,
        parent,
        text,
        command,
        color
    ):

        button = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Segoe UI", 8, "bold"),
            bg="#1B2744",
            fg=color,
            activebackground=color,
            activeforeground="#050816",
            relief="flat",
            bd=0,
            cursor="hand2"
        )

        button.pack(
            side="left",
            fill="x",
            expand=True,
            padx=2,
            ipady=8
        )

        # Hover effect

        def enter(event):
            button.configure(
                bg="#26385F"
            )

        def leave(event):
            button.configure(
                bg="#1B2744"
            )

        button.bind(
            "<Enter>",
            enter
        )

        button.bind(
            "<Leave>",
            leave
        )

    # ========================================================
    # DRAW ARENA
    # ========================================================

    def draw_arena(self):

        if not hasattr(
            self,
            "arena_canvas"
        ):
            return

        canvas = self.arena_canvas

        canvas.delete("all")

        width = canvas.winfo_width()

        if width < 100:
            width = 650

        # ----------------------------------------------------
        # Decorative center
        # ----------------------------------------------------

        canvas.create_text(
            width / 2,
            102,
            text="VS",
            fill="#33415F",
            font=("Segoe UI", 16, "bold")
        )

        canvas.create_text(
            width / 2,
            125,
            text="HUMAN",
            fill="#263451",
            font=("Segoe UI", 7, "bold")
        )

        # ----------------------------------------------------
        # JUGS
        # ----------------------------------------------------

        self.draw_big_jug(
            canvas,
            width * 0.27,
            25,
            185,
            125,
            self.user_a,
            max(1, self.capacity_a.get()),
            "JUG A",
            self.CYAN
        )

        self.draw_big_jug(
            canvas,
            width * 0.73,
            25,
            185,
            125,
            self.user_b,
            max(1, self.capacity_b.get()),
            "JUG B",
            self.PURPLE
        )

    # ========================================================
    # BIG JUG
    # ========================================================

    def draw_big_jug(
        self,
        canvas,
        center,
        top,
        bottom,
        width,
        amount,
        capacity,
        name,
        accent
    ):

        left = center - width / 2
        right = center + width / 2

        # Glow layers

        canvas.create_rectangle(
            left - 5,
            top - 5,
            right + 5,
            bottom + 5,
            outline="#172747",
            width=4
        )

        # Main glass

        canvas.create_rectangle(
            left,
            top,
            right,
            bottom,
            outline=accent,
            width=3
        )

        # Water

        ratio = 0

        if capacity > 0:
            ratio = min(
                amount / capacity,
                1
            )

        water_height = (
            bottom - top
        ) * ratio

        water_top = bottom - water_height

        if water_height > 0:

            canvas.create_rectangle(
                left + 3,
                water_top,
                right - 3,
                bottom - 3,
                fill=self.WATER,
                outline=""
            )

            # Water highlights

            canvas.create_line(
                left + 4,
                water_top + 3,
                right - 4,
                water_top + 3,
                fill=self.WATER_LIGHT,
                width=2
            )

            canvas.create_line(
                left + 15,
                water_top + 10,
                left + 45,
                water_top + 10,
                fill="#A5F3FC",
                width=1
            )

        # Name

        canvas.create_text(
            center,
            top - 13,
            text=name,
            fill=accent,
            font=("Segoe UI", 11, "bold")
        )

        # Amount

        canvas.create_text(
            center,
            105,
            text=f"{amount} L",
            fill=self.WHITE,
            font=("Segoe UI", 23, "bold")
        )

        # Capacity

        canvas.create_text(
            center,
            bottom + 13,
            text=f"MAX {capacity} L",
            fill=self.GRAY,
            font=("Segoe UI", 8, "bold")
        )

    # ========================================================
    # SOLUTION
    # ========================================================

    def create_solution(self, parent):

        panel = tk.Frame(
            parent,
            bg=self.PANEL,
            highlightbackground="#27365A",
            highlightthickness=1
        )

        panel.pack(
            fill="both",
            expand=True,
            pady=(12, 0)
        )

        header = tk.Frame(
            panel,
            bg=self.PANEL
        )

        header.pack(
            fill="x",
            padx=20,
            pady=12
        )

        tk.Label(
            header,
            text="🧠 AI BATTLE PLAN",
            font=("Segoe UI", 10, "bold"),
            bg=self.PANEL,
            fg=self.PINK
        ).pack(
            side="left"
        )

        self.solution_status = tk.Label(
            header,
            text="AI waiting...",
            font=("Segoe UI", 8, "bold"),
            bg=self.PANEL,
            fg=self.GRAY
        )

        self.solution_status.pack(
            side="right"
        )

        # List

        frame = tk.Frame(
            panel,
            bg=self.PANEL
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=18,
            pady=(0, 15)
        )

        scroll = tk.Scrollbar(
            frame
        )

        scroll.pack(
            side="right",
            fill="y"
        )

        self.solution_list = tk.Listbox(
            frame,
            bg="#080E1E",
            fg="#CFFAFE",
            selectbackground="#164E63",
            selectforeground=self.WHITE,
            font=("Consolas", 9),
            relief="flat",
            bd=0,
            highlightthickness=1,
            highlightbackground="#1D2A47",
            yscrollcommand=scroll.set
        )

        self.solution_list.pack(
            side="left",
            fill="both",
            expand=True
        )

        scroll.config(
            command=self.solution_list.yview
        )

        self.solution_list.insert(
            tk.END,
            "  AI PATH  →  Generate a solution to begin"
        )

    # ========================================================
    # CONTROL PANEL
    # ========================================================

    def create_control_panel(self, parent):

        panel = tk.Frame(
            parent,
            bg=self.PANEL,
            highlightbackground="#27365A",
            highlightthickness=1
        )

        panel.pack(
            fill="x"
        )

        tk.Label(
            panel,
            text="⚙  GAME SETTINGS",
            font=("Segoe UI", 10, "bold"),
            bg=self.PANEL,
            fg=self.WHITE
        ).pack(
            anchor="w",
            padx=20,
            pady=(17, 12)
        )

        self.create_input(
            panel,
            "JUG A CAPACITY",
            self.capacity_a
        )

        self.create_input(
            panel,
            "JUG B CAPACITY",
            self.capacity_b
        )

        self.create_input(
            panel,
            "TARGET AMOUNT",
            self.target
        )

        # Start

        self.start_button = tk.Button(
            panel,
            text="⚡  NEW CHALLENGE",
            command=self.new_game,
            font=("Segoe UI", 9, "bold"),
            bg=self.BLUE,
            fg="#04111E",
            activebackground="#67E8F9",
            relief="flat",
            bd=0,
            cursor="hand2"
        )

        self.start_button.pack(
            fill="x",
            padx=20,
            pady=(15, 7),
            ipady=9
        )

        # AI solution

        self.solve_button = tk.Button(
            panel,
            text="🤖  GENERATE AI SOLUTION",
            command=self.solve_ai,
            font=("Segoe UI", 9, "bold"),
            bg="#25345A",
            fg=self.PINK,
            activebackground="#374B78",
            relief="flat",
            bd=0,
            cursor="hand2"
        )

        self.solve_button.pack(
            fill="x",
            padx=20,
            pady=(0, 7),
            ipady=9
        )

        # Watch AI

        self.watch_button = tk.Button(
            panel,
            text="▶  WATCH AI PLAY",
            command=self.watch_ai,
            font=("Segoe UI", 9, "bold"),
            bg="#251D42",
            fg=self.PURPLE,
            activebackground="#392E61",
            relief="flat",
            bd=0,
            cursor="hand2",
            state="disabled"
        )

        self.watch_button.pack(
            fill="x",
            padx=20,
            pady=(0, 18),
            ipady=9
        )

    # ========================================================
    # INPUT
    # ========================================================

    def create_input(
        self,
        parent,
        text,
        variable
    ):

        row = tk.Frame(
            parent,
            bg=self.PANEL
        )

        row.pack(
            fill="x",
            padx=20,
            pady=4
        )

        tk.Label(
            row,
            text=text,
            font=("Segoe UI", 8, "bold"),
            bg=self.PANEL,
            fg=self.GRAY
        ).pack(
            side="left"
        )

        entry = tk.Entry(
            row,
            textvariable=variable,
            width=7,
            font=("Segoe UI", 10, "bold"),
            bg="#080E1E",
            fg=self.CYAN,
            insertbackground=self.CYAN,
            justify="center",
            relief="flat"
        )

        entry.pack(
            side="right",
            ipady=4
        )

    # ========================================================
    # AI PANEL
    # ========================================================

    def create_ai_panel(self, parent):

        panel = tk.Frame(
            parent,
            bg=self.PANEL,
            highlightbackground="#27365A",
            highlightthickness=1
        )

        panel.pack(
            fill="x",
            pady=(12, 0)
        )

        tk.Label(
            panel,
            text="🤖 AI CORE",
            font=("Segoe UI", 10, "bold"),
            bg=self.PANEL,
            fg=self.PINK
        ).pack(
            anchor="w",
            padx=20,
            pady=(16, 10)
        )

        self.create_ai_info(
            panel,
            "CURRENT STATE",
            "(0, 0)",
            "ai_state"
        )

        self.create_ai_info(
            panel,
            "SHORTEST PATH",
            "0 moves",
            "ai_path"
        )

        self.create_ai_info(
            panel,
            "STATES EXPLORED",
            "0",
            "ai_explored"
        )

        self.create_ai_info(
            panel,
            "AI STATUS",
            "STANDBY",
            "ai_status"
        )

        # Explanation

        tk.Label(
            panel,
            text=(
                "BFS explores the state space\n"
                "level-by-level and searches for\n"
                "the shortest valid solution."
            ),
            font=("Segoe UI", 8),
            justify="left",
            bg=self.PANEL,
            fg=self.GRAY
        ).pack(
            anchor="w",
            padx=20,
            pady=(10, 15)
        )

    # ========================================================
    # AI INFO
    # ========================================================

    def create_ai_info(
        self,
        parent,
        title,
        value,
        name
    ):

        row = tk.Frame(
            parent,
            bg=self.PANEL
        )

        row.pack(
            fill="x",
            padx=20,
            pady=3
        )

        tk.Label(
            row,
            text=title,
            font=("Segoe UI", 8),
            bg=self.PANEL,
            fg=self.GRAY
        ).pack(
            side="left"
        )

        label = tk.Label(
            row,
            text=value,
            font=("Segoe UI", 8, "bold"),
            bg=self.PANEL,
            fg=self.WHITE
        )

        label.pack(
            side="right"
        )

        setattr(
            self,
            name,
            label
        )

    # ========================================================
    # HUMAN ACTIONS
    # ========================================================

    def fill_a(self):

        if self.game_finished:
            return

        capacity = self.capacity_a.get()

        if self.user_a == capacity:
            self.flash_invalid()
            return

        self.user_a = capacity

        self.user_move()

    # --------------------------------------------------------

    def fill_b(self):

        if self.game_finished:
            return

        capacity = self.capacity_b.get()

        if self.user_b == capacity:
            self.flash_invalid()
            return

        self.user_b = capacity

        self.user_move()

    # --------------------------------------------------------

    def empty_a(self):

        if self.game_finished:
            return

        if self.user_a == 0:
            self.flash_invalid()
            return

        self.user_a = 0

        self.user_move()

    # --------------------------------------------------------

    def empty_b(self):

        if self.game_finished:
            return

        if self.user_b == 0:
            self.flash_invalid()
            return

        self.user_b = 0

        self.user_move()

    # --------------------------------------------------------

    def pour_a_b(self):

        if self.game_finished:
            return

        amount = min(
            self.user_a,
            self.capacity_b.get() - self.user_b
        )

        if amount <= 0:
            self.flash_invalid()
            return

        self.user_a -= amount
        self.user_b += amount

        self.user_move()

    # --------------------------------------------------------

    def pour_b_a(self):

        if self.game_finished:
            return

        amount = min(
            self.user_b,
            self.capacity_a.get() - self.user_a
        )

        if amount <= 0:
            self.flash_invalid()
            return

        self.user_b -= amount
        self.user_a += amount

        self.user_move()

    # ========================================================
    # USER MOVE
    # ========================================================

    def user_move(self):

        self.user_moves += 1

        self.update_everything()

        # Goal

        if (
            self.user_a == self.target.get()
            or
            self.user_b == self.target.get()
        ):

            self.user_wins()

    # ========================================================
    # INVALID MOVE
    # ========================================================

    def flash_invalid(self):

        self.status_label.config(
            text="INVALID MOVE",
            fg=self.YELLOW
        )

        self.status_light.config(
            fg=self.YELLOW
        )

        self.root.after(
            1000,
            self.restore_status
        )

    # ========================================================
    # RESTORE
    # ========================================================

    def restore_status(self):

        if not self.game_finished:

            self.status_label.config(
                text="SYSTEM READY",
                fg=self.GREEN
            )

            self.status_light.config(
                fg=self.GREEN
            )

    # ========================================================
    # USER WINS
    # ========================================================

    def user_wins(self):

        self.game_finished = True

        self.user_score += 1

        self.status_label.config(
            text="🎉 TARGET REACHED!",
            fg=self.GREEN
        )

        self.status_light.config(
            fg=self.GREEN
        )

        self.ai_status.config(
            text="RESULT READY"
        )

        # Calculate AI if not already

        if not self.ai_solution:

            self.solve_ai(
                show_message=False
            )

        ai_moves = len(
            self.ai_solution
        )

        if self.user_moves <= ai_moves:

            result = (
                "🏆 HUMAN WINS!\n\n"
                f"Your moves: {self.user_moves}\n"
                f"AI shortest: {ai_moves}\n\n"
                "You matched or beat the AI!"
            )

        else:

            result = (
                "🎯 TARGET REACHED!\n\n"
                f"Your moves: {self.user_moves}\n"
                f"AI shortest: {ai_moves}\n\n"
                "The AI found a more efficient path.\n"
                "Try again and beat it!"
            )

        messagebox.showinfo(
            "Challenge Complete",
            result
        )

    # ========================================================
    # BFS
    # ========================================================

    def bfs(
        self,
        capacity_a,
        capacity_b,
        target
    ):

        start = (0, 0)

        queue = deque(
            [start]
        )

        visited = {
            start
        }

        parent = {}

        actions = {}

        explored = []

        while queue:

            current = queue.popleft()

            explored.append(
                current
            )

            a, b = current

            # Goal test

            if (
                a == target
                or
                b == target
            ):

                path = []

                state = current

                while state != start:

                    path.append(
                        (
                            actions[state],
                            state
                        )
                    )

                    state = parent[state]

                path.reverse()

                return path, explored

            # ------------------------------------------------
            # OPERATORS
            # ------------------------------------------------

            possibilities = []

            # Fill A

            possibilities.append(
                (
                    (capacity_a, b),
                    "Fill Jug A"
                )
            )

            # Fill B

            possibilities.append(
                (
                    (a, capacity_b),
                    "Fill Jug B"
                )
            )

            # Empty A

            possibilities.append(
                (
                    (0, b),
                    "Empty Jug A"
                )
            )

            # Empty B

            possibilities.append(
                (
                    (a, 0),
                    "Empty Jug B"
                )
            )

            # Pour A -> B

            amount = min(
                a,
                capacity_b - b
            )

            possibilities.append(
                (
                    (a - amount, b + amount),
                    "Pour A → B"
                )
            )

            # Pour B -> A

            amount = min(
                b,
                capacity_a - a
            )

            possibilities.append(
                (
                    (a + amount, b - amount),
                    "Pour B → A"
                )
            )

            # ------------------------------------------------
            # ADD NEW STATES
            # ------------------------------------------------

            for new_state, operation in possibilities:

                if new_state not in visited:

                    visited.add(
                        new_state
                    )

                    parent[new_state] = current

                    actions[new_state] = operation

                    queue.append(
                        new_state
                    )

        return None, explored

    # ========================================================
    # SOLVE AI
    # ========================================================

    def solve_ai(
        self,
        show_message=True
    ):

        try:

            a = self.capacity_a.get()
            b = self.capacity_b.get()
            target = self.target.get()

        except:

            messagebox.showerror(
                "Invalid Input",
                "Enter valid numbers."
            )

            return

        if (
            a <= 0
            or
            b <= 0
            or
            target <= 0
        ):

            messagebox.showerror(
                "Invalid Input",
                "Values must be greater than zero."
            )

            return

        if target > max(a, b):

            messagebox.showerror(
                "Impossible",
                "Target is larger than both jugs."
            )

            return

        result, explored = self.bfs(
            a,
            b,
            target
        )

        self.ai_states_explored = len(
            explored
        )

        if result is None:

            self.ai_solution = []

            self.solution_status.config(
                text="NO SOLUTION",
                fg=self.RED
            )

            self.watch_button.config(
                state="disabled"
            )

            self.ai_status.config(
                text="NO SOLUTION",
                fg=self.RED
            )

            return

        self.ai_solution = result

        self.ai_step = 0

        self.ai_a = 0
        self.ai_b = 0

        # ----------------------------------------------------
        # Display
        # ----------------------------------------------------

        self.solution_list.delete(
            0,
            tk.END
        )

        self.solution_list.insert(
            tk.END,
            "  00   START STATE             → (0, 0)"
        )

        for index, (
            operation,
            state
        ) in enumerate(
            self.ai_solution,
            start=1
        ):

            self.solution_list.insert(
                tk.END,
                f"  {index:02d}   "
                f"{operation:<22} → {state}"
            )

        # ----------------------------------------------------
        # UI
        # ----------------------------------------------------

        self.solution_status.config(
            text=f"{len(self.ai_solution)} MOVES",
            fg=self.GREEN
        )

        self.watch_button.config(
            state="normal"
        )

        self.ai_status.config(
            text="SOLUTION READY",
            fg=self.GREEN
        )

        if show_message:

            messagebox.showinfo(
                "AI Analysis Complete",
                f"BFS found the shortest path!\n\n"
                f"Shortest moves: {len(self.ai_solution)}\n"
                f"States explored: {self.ai_states_explored}"
            )

        self.update_everything()

    # ========================================================
    # WATCH AI
    # ========================================================

    def watch_ai(self):

        if not self.ai_solution:

            self.solve_ai(
                show_message=False
            )

        if not self.ai_solution:
            return

        self.ai_running = True

        self.ai_a = 0
        self.ai_b = 0
        self.ai_step = 0

        self.animate_ai()

    # ========================================================
    # AI ANIMATION
    # ========================================================

    def animate_ai(self):

        if not self.ai_running:
            return

        if self.ai_step >= len(
            self.ai_solution
        ):

            self.ai_running = False

            self.ai_status.config(
                text="GOAL REACHED",
                fg=self.GREEN
            )

            return

        operation, state = self.ai_solution[
            self.ai_step
        ]

        self.ai_a = state[0]
        self.ai_b = state[1]

        self.ai_step += 1

        # Highlight current AI step

        self.solution_list.selection_clear(
            0,
            tk.END
        )

        self.solution_list.selection_set(
            self.ai_step
        )

        self.solution_list.see(
            self.ai_step
        )

        self.ai_status.config(
            text=f"STEP {self.ai_step}",
            fg=self.CYAN
        )

        self.update_everything()

        self.root.after(
            700,
            self.animate_ai
        )

    # ========================================================
    # NEW GAME
    # ========================================================

    def new_game(self):

        self.ai_running = False

        self.game_finished = False

        self.user_a = 0
        self.user_b = 0

        self.user_moves = 0

        self.ai_a = 0
        self.ai_b = 0

        self.ai_moves = 0

        self.ai_solution = []

        self.ai_step = 0

        self.ai_states_explored = 0

        self.solution_list.delete(
            0,
            tk.END
        )

        self.solution_list.insert(
            tk.END,
            "  AI PATH  →  Generate a solution to begin"
        )

        self.solution_status.config(
            text="AI waiting...",
            fg=self.GRAY
        )

        self.ai_status.config(
            text="STANDBY",
            fg=self.GRAY
        )

        self.watch_button.config(
            state="disabled"
        )

        self.status_label.config(
            text="SYSTEM READY",
            fg=self.GREEN
        )

        self.status_light.config(
            fg=self.GREEN
        )

        self.update_everything()

    # ========================================================
    # UPDATE
    # ========================================================

    def update_everything(self):

        # Human

        if hasattr(
            self,
            "player_state"
        ):

            self.player_state.config(
                text=f"STATE  ({self.user_a}, {self.user_b})"
            )

        # Target

        if hasattr(
            self,
            "target_badge"
        ):

            self.target_badge.config(
                text=f"🎯 TARGET: {self.target.get()} LITRES"
            )

        # Statistics

        if hasattr(
            self,
            "user_stat"
        ):

            self.user_stat.config(
                text=str(
                    self.user_moves
                )
            )

        if hasattr(
            self,
            "ai_stat"
        ):

            self.ai_stat.config(
                text=str(
                    len(self.ai_solution)
                )
            )

        if hasattr(
            self,
            "state_stat"
        ):

            self.state_stat.config(
                text=str(
                    self.ai_states_explored
                )
            )

        if hasattr(
            self,
            "target_stat"
        ):

            self.target_stat.config(
                text=f"{self.target.get()} L"
            )

        # AI

        if hasattr(
            self,
            "ai_state"
        ):

            self.ai_state.config(
                text=f"({self.ai_a}, {self.ai_b})"
            )

        if hasattr(
            self,
            "ai_path"
        ):

            self.ai_path.config(
                text=f"{len(self.ai_solution)} moves"
            )

        if hasattr(
            self,
            "ai_explored"
        ):

            self.ai_explored.config(
                text=str(
                    self.ai_states_explored
                )
            )

        # Draw

        self.draw_arena()


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = AquaMindGame(
        root
    )

    root.mainloop()
