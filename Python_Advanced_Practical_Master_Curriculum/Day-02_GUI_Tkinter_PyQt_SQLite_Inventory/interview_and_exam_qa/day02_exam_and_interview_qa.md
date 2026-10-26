# Day 2: GUI Exam & Top Placement Interview Q&A

### Q1: Why does a Tkinter or PyQt GUI freeze when performing network requests or long loops?
- **Answer**: GUIs run an **Event Loop** (`mainloop()` or `app.exec()`) on the application's primary OS thread (Main Thread). This thread handles redraw events, button clicks, and mouse hovering at 60 FPS. If you perform a blocking operation (like `time.sleep()`, file download, or SQL query) on the main thread, the event loop stops processing window events, causing the OS to report the window as "(Not Responding)".
- **Solution**: Execute blocking tasks inside a background worker thread (`threading.Thread` or `QThread`).

### Q2: What are the differences between Tkinter's geometry managers: `pack()`, `grid()`, and `place()`?
- **Answer**:
  - `pack()`: Arranges widgets along edges (TOP, BOTTOM, LEFT, RIGHT). Best for simple vertical/horizontal toolbars.
  - `grid()`: Arranges widgets in a 2D table of rows and columns. Most versatile and industry-standard for enterprise forms.
  - `place()`: Positions widgets at absolute pixel coordinates (`x`, `y`). Not recommended for responsive design across different screen resolutions.
