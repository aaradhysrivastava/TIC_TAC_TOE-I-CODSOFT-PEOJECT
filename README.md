<!DOCTYPE html>

<h1>🎮 Tic-Tac-Toe AI Project</h1>
<p>This project is a Python-based Tic-Tac-Toe game with an unbeatable AI, built using the <strong>Minimax algorithm with Alpha-Beta pruning</strong>. It includes a GUI, sound effects, and difficulty levels.</p>

<h2>🧠 Features</h2>
<ul>
  <li>Play against an AI using the Minimax algorithm</li>
  <li>Three difficulty levels: Easy, Medium, and Hard</li>
  <li>Simple sound effects on each move (via <code>winsound</code> for Windows)</li>
  <li>Real-time game timer displayed in the GUI</li>
  <li>Automatic reset after win, loss, or tie</li>
  <li>Interactive graphical interface built with Tkinter</li>
</ul>

<h2>🛠️ Technologies & Concepts Used</h2>
<ul>
  <li><strong>Python 3</strong> — Primary programming language</li>
  <li><strong>Tkinter</strong> — For building the GUI</li>
  <li><strong>Minimax Algorithm</strong> — Used for making AI unbeatable</li>
  <li><strong>Alpha-Beta Pruning</strong> — Optimizes Minimax to reduce computation</li>
  <li><strong>winsound</strong> — Plays move sounds (Windows only)</li>
  <li><strong>pygame (optional)</strong> — Use for sound on macOS/Linux</li>
  <li><strong>Random module</strong> — For "Easy" and "Medium" AI strategies</li>
  <li><strong>Time & after()</strong> — Timer logic for tracking game duration</li>
</ul>

<h2>📂 Project Structure</h2>
<pre>
TIC_TAC_TOE_AI_PROJECT/
├── TIC_TAC_TOE_AI.py
├── README.md
└── Tic-Tac-Toe AI Project DESCRIPTION.txt
</pre>

<h2>▶️ How to Run</h2>
<ol>
  <li>Make sure Python 3 is installed on your system.</li>
  <li>Clone or download the repository.</li>
  <li>Run the script:
    <pre><code>python TIC_TAC_TOE_AI.py</code></pre>
  </li>
  <li>(Optional) Install pygame for cross-platform sound support:
    <pre><code>pip install pygame</code></pre>
  </li>
</ol>

<h2>🧪 Example Gameplay</h2>
<pre>
[You click a cell] → "X" appears
[AI responds]      → "O" appears and sound plays
[Timer running...]
[Result shown]     → "You Win!" or "AI Wins!" or "It's a Tie!"
</pre>

<h2>👨‍💻 Author</h2>
<p>Made with ❤️ in Python by <strong>Aaradhy Srivastava</strong>.</p>

</body>
</html>
