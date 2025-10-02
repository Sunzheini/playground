from nicegui import ui


# elements & tailwind classes:
"""
## Common elements

### Input Elements
ui.button("Click me", on_click=handler)	             <button onclick="handler()">Click me</button>	        Interactive button
ui.input(label="Text input", placeholder="123")	     <input type="text" placeholder="123">	                Single-line text input
ui.textarea(label="Multi-line", placeholder="123")	 <textarea placeholder="123"></textarea>	            Multi-line text input
ui.number(label="Number", value=42, min=0, max=100)	 <input type="number" value="42" min="0" max="100">	    Numeric input
ui.slider(min=0, max=100, value=50)	                 <input type="range" min="0" max="100" value="50">	    Range slider
ui.toggle(options=['Option A', 'Option B'])	         Radio button group or custom toggle	                Option selector
ui.checkbox("Check me")	                             <input type="checkbox"> Check me	                    Checkbox input
ui.switch("Toggle me")	                             <input type="checkbox" class="toggle"> Toggle me	    Toggle switch
ui.select(options=['A', 'B'], value='A')	         <select><option>A</option><option>B</option></select>	Dropdown selection
ui.radio(options=['Red', 'Green'], value='Red')	     Radio button group	                                    Radio button group
ui.date(value='2023-12-01')	                         <input type="date" value="2023-12-01">	                Date picker
ui.time(value='14:30')	                             <input type="time" value="14:30">	                    Time picker
ui.upload(label="File upload", on_upload=handler)	 <input type="file" onchange="handler()">	            File upload

### Display Elements
ui.label("Simple text display")                      <div>Simple text display</div>                         Text display
ui.markdown("# Markdown **support**")                <h1>Markdown <strong>support</strong></h1>             Markdown content
ui.html("<div>Raw HTML</div>")                       <div>Raw HTML</div>                                    Direct HTML injection
ui.icon("thumb_up")                                  <i class="material-icons">thumb_up</i>                 Material icon
ui.image("https://picsum.photos/200")                <img src="https://picsum.photos/200">                  Image display
ui.avatar("JD", color="blue")                        <div class="avatar blue">JD</div>                      User avatar
ui.spinner(size="lg")                                <div class="spinner large"></div>                      Loading indicator
ui.linear_progress(value=0.5)                        <progress value="0.5" max="1">                         Progress bar
ui.circular_progress(value=75)                       SVG circle animation                                   Circular progress
ui.separator()                                       <hr>                                                   Horizontal divider
ui.badge("New", color="red")                         <span class="badge red">New</span>                     Status badge

### Layout containers
ui.row()                                             <div style="display: flex;">                           Horizontal flex container
ui.column()                                          <div style="display: flex; flex-direction: column;">   Vertical flex container
ui.grid(columns=3)                                   <div style="display: grid; grid-template-columns: repeat(3, 1fr);">    CSS Grid container
ui.card()                                            <div class="card">                                     Card with shadow/border
ui.expansion("Title")                                <details><summary>Title</summary>                      Expandable section

### Navigation & Structure
ui.tabs()                                            <div class="tabs"><nav>...</nav><div class="content">...</div></div>   Tab navigation
ui.stepper()                                         Multi-step form markup                                 Step-by-step form
ui.scroll_area()                                     <div style="overflow: auto;">                          Scrollable container
ui.splitter()                                        Resizable split panes                                  Panel divider

### Data Display
ui.table(columns=['Name', 'Age'], rows=[...])        <table><tr><th>Name</th><th>Age</th></tr>...</table>   Data table
ui.aggrid.from_pandas(df)                            Advanced JS grid component                             Interactive data grid
ui.chart({...})                                      <canvas> with Chart.js                                 Chart.js charts
ui.plotly(fig)                                       Plotly.js div                                          Plotly charts
ui.pyplot(fig)                                       <img src="data:image/png;base64,...">                  Matplotlib figures
ui.echart({...})                                     ECharts div                                            ECharts visualization

### Interactive & Feedback
ui.notify("Message")                                 Toast notification div                                 Popup message
ui.dialog()                                          <dialog> or modal div                                  Modal dialog
ui.menu()                                            <nav><ul><li>...</li></ul></nav>                       Dropdown menu
ui.tooltip("Help text")                              <div class="tooltip">Help text</div>                   Hover tooltip
ui.link("Go to page", "/page")                       <a href="/page">Go to page</a>                         Hyperlink
ui.button("Navigate", on_click=ui.open("/target"))   <button onclick="window.location='/target'">Navigate</button>    Navigation button

### Media & Files
ui.audio("audio.mp3")                                <audio controls><source src="audio.mp3"></audio>       Audio player
ui.video("video.mp4")                                <video controls><source src="video.mp4"></video>       Video player
ui.download("data.txt", "Hello World")               <a download="data.txt" href="data:text/plain,Hello World">Download</a>    File download

### Advanced Components
ui.tree([...])                                       Nested <ul><li> structure                              Tree view component
ui.timeline([...])                                   Timeline markup                                        Timeline display
ui.jupyter(code)                                     Code execution iframe                                  Code execution
ui.json({...})                                       <pre>{...}</pre>                                       JSON viewer


## tailwind classes:
### Width
.classes('w-full')                width: 100%;                                  100% width
.classes('w-1/2')                 width: 50%;                                   50% width
.classes('w-1/3')                 width: 33.333333%;                            33% width
.classes('w-64')                  width: 16rem;                                 256px width
.classes('w-auto')                width: auto;                                  auto width
.classes('max-w-md')              max-width: 28rem;                             max-width: 28rem (448px)
.classes('max-w-lg')              max-width: 32rem;                             max-width: 32rem (512px)

### Height
.classes('h-screen')              height: 100vh;                                100vh height
.classes('h-full')                height: 100%;                                 100% height
.classes('h-64')                  height: 16rem;                                256px height

### Padding
.classes('p-2')                   padding: 0.5rem;                              8px padding
.classes('p-4')                   padding: 1rem;                                16px padding (most common)
.classes('p-6')                   padding: 1.5rem;                              24px padding
.classes('px-4')                  padding-left: 1rem; padding-right: 1rem;      16px left/right
.classes('py-2')                  padding-top: 0.5rem; padding-bottom: 0.5rem;  8px top/bottom
.classes('pt-4')                  padding-top: 1rem;                            16px top only
.classes('pb-2')                  padding-bottom: 0.5rem;                       8px bottom only

### Margin
.classes('m-2')                   margin: 0.5rem;                               8px margin
.classes('m-4')                   margin: 1rem;                                 16px margin
.classes('mx-auto')               margin-left: auto; margin-right: auto;        center horizontally
.classes('my-4')                  margin-top: 1rem; margin-bottom: 1rem;        16px top/bottom margin
.classes('mt-2')                  margin-top: 0.5rem;                           8px top margin
.classes('mb-4')                  margin-bottom: 1rem;                          16px bottom margin
.classes('ml-[355px]')            margin-left: 355px;                           355px left margin (arbitrary value)

### Gap
.classes('gap-2')                 gap: 0.5rem;                                  8px gap (small)
.classes('gap-4')                 gap: 1rem;                                    16px gap (medium - most common)
.classes('gap-6')                 gap: 1.5rem;                                  24px gap (large)

### Primary colors
.classes('bg-blue-500')           background-color: #3b82f6;                    Medium blue
.classes('bg-green-500')          background-color: #22c55e;                    Medium green
.classes('bg-red-500')            background-color: #ef4444;                    Medium red
.classes('bg-yellow-500')         background-color: #eab308;                    Medium yellow
.classes('bg-purple-500')         background-color: #a855f7;                    Medium purple
.classes('bg-gray-500')           background-color: #6b7280;                    Medium gray

### Light backgrounds
.classes('bg-blue-50')            background-color: #eff6ff;                    Very light blue
.classes('bg-gray-50')            background-color: #f9fafb;                    Very light gray
.classes('bg-green-50')           background-color: #f0fdf4;                    Very light green
.classes('bg-white')              background-color: #fff;                       White
.classes('bg-transparent')        background-color: transparent;                Transparent

### Text Colors
.classes('text-white')            color: #fff;                                  White text
.classes('text-black')            color: #000;                                  Black text
.classes('text-gray-600')         color: #4b5563;                               Dark gray text
.classes('text-gray-400')         color: #9ca3af;                               Light gray text
.classes('text-blue-600')         color: #2563eb;                               Blue text
.classes('text-red-600')          color: #dc2626;                               Red text

### Borders and Radius
.classes('border')                border-width: 1px;                            1px border
.classes('border-2')              border-width: 2px;                            2px border
.classes('border-gray-300')       border-color: #d1d5db;                        Light gray border
.classes('border-blue-500')       border-color: #3b82f6;                        Blue border
.classes('rounded')               border-radius: 0.25rem;                       Small border radius
.classes('rounded-lg')            border-radius: 0.5rem;                        Large border radius
.classes('rounded-full')          border-radius: 9999px;                        Full rounded (circles)

### Shadows
.classes('shadow')                box-shadow: 0 1px 3px 0 #0000001a, 0 1px 2px 0 #0000000f;             Small shadow
.classes('shadow-md')             box-shadow: 0 4px 6px -1px #0000001a, 0 2px 4px -1px #0000000f;       Medium shadow
.classes('shadow-lg')             box-shadow: 0 10px 15px -3px #0000001a, 0 4px 6px -2px #0000000f;     Large shadow
.classes('shadow-none')           box-shadow: none;                                                     No shadow

### Text size
.classes('text-sm')               font-size: 0.875rem; line-height: 1.25rem;    Small text
.classes('text-base')             font-size: 1rem; line-height: 1.5rem;         Base text (default)
.classes('text-lg')               font-size: 1.125rem; line-height: 1.75rem;    Large text
.classes('text-xl')               font-size: 1.25rem; line-height: 1.75rem;     Extra large
.classes('text-2xl')              font-size: 1.5rem; line-height: 2rem;         2x large
.classes('text-3xl')              font-size: 1.875rem; line-height: 2.25rem;    3x large

### Font Weight
.classes('font-normal')           font-weight: 400;                             Normal weight
.classes('font-medium')           font-weight: 500;                             Medium weight
.classes('font-bold')             font-weight: 700;                             Bold (most common)
.classes('font-semibold')         font-weight: 600;                             Semi-bold

### Text Alignment
.classes('text-left')             text-align: left;                             Left align
.classes('text-center')           text-align: center;                           Center align (common)
.classes('text-right')            text-align: right;                            Right align

### Flexbox (align-items is vertical, justify-content is horizontal)
.classes('flex')                  display: flex;                                Display flex
.classes('flex-col')              flex-direction: column;                       Flex column
.classes('flex-row')              flex-direction: row;                          Flex row (default)
.classes('items-start')           align-items: flex-start;                      Vertical start (default)
.classes('items-end')             align-items: flex-end;                        Vertical end
.classes('items-center')          align-items: center;                          Vertical center
.classes('items-baseline')        align-items: baseline;                        Baseline alignment
.classes('items-stretch')         align-items: stretch; (default)               Height stretch (default)
.classes('justify-start')         justify-content: flex-start;                  Horizontal start
.classes('justify-end')           justify-content: flex-end;                    Horizontal end
.classes('justify-center')        justify-content: center;                      Horizontal center
.classes('justify-between')       justify-content: space-between;               Space between
.classes('justify-around')        justify-content: space-around;                Space around
.classes('justify-evenly')        justify-content: space-evenly;                Even spacing

### Grid
.classes('grid')                  display: grid;                                Display grid
.classes('grid-cols-2')           grid-template-columns: repeat(2, minmax(0, 1fr));     2 columns
.classes('grid-cols-3')           grid-template-columns: repeat(3, minmax(0, 1fr));     3 columns
.classes('grid-cols-4')           grid-template-columns: repeat(4, minmax(0, 1fr));     4 columns

### Hover Effects
.classes('hover:bg-blue-600')     (on hover) background-color: #2563eb;                                             Darker blue on hover
.classes('hover:shadow-lg')       (on hover) box-shadow: 0 10px 15px -3px #0000001a, 0 4px 6px -2px #0000000f;      Larger shadow on hover
.classes('hover:scale-105')       (on hover) transform: scale(1.05);                                                Slight scale on hover

### Opacity
.classes('opacity-50')            opacity: 0.5;                                 50% opacity
.classes('opacity-75')            opacity: 0.75;                                75% opacity
.classes('opacity-100')           opacity: 1;                                   100% opacity (normal)

### COMMON COMBINATIONS: Cards
.classes('p-4 bg-white rounded shadow')         
padding: 1rem; background-color: #fff; border-radius: 0.25rem; box-shadow: 0 1px 3px 0 #0000001a, 0 1px 2px 0 #0000000f;    
Basic card

.classes('p-6 bg-gray-50 rounded-lg border')    
padding: 1.5rem; background-color: #f9fafb; border-radius: 0.5rem; border-width: 1px;                                       
Fancy card

### COMMON COMBINATIONS: Buttons
.classes('px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600')   
padding-left: 1rem; padding-right: 1rem; padding-top: 0.5rem; padding-bottom: 0.5rem; background-color: #3b82f6; color: #fff; border-radius: 0.25rem; (on hover) background-color: #2563eb;    
Primary button

.classes('px-3 py-1 bg-gray-200 text-gray-800 rounded')                  
padding-left: 0.75rem; padding-right: 0.75rem; padding-top: 0.25rem; padding-bottom: 0.25rem; background-color: #e5e7eb; color: #1f2937; border-radius: 0.25rem;                               
Secondary button

with ui.button('Options', icon='menu'):
    with ui.menu():  # This creates the dropdown
        ui.menu_item('Edit')
        ui.menu_item('Delete')
        ui.separator()
        ui.menu_item('Settings')

ui.button('Options', icon='menu' on_click=lambda: click(number, default_text)).classes('px-3 py-1 bg-gray-200 text-gray-800 rounded hover:bg-gray-300')

### COMMON COMBINATIONS: Inputs
.classes('p-2 border rounded w-full')           
padding: 0.5rem; border-width: 1px; border-radius: 0.25rem; width: 100%;   
Full width input

.classes('px-3 py-2 border rounded')            
padding-left: 0.75rem; padding-right: 0.75rem; padding-top: 0.5rem; padding-bottom: 0.5rem; border-width: 1px; border-radius: 0.25rem;   
Standard input

### COMMON COMBINATIONS: Layouts
.classes('w-full p-4')                          
width: 100%; padding: 1rem;   
Full width section

.classes('max-w-2xl mx-auto p-6')               
max-width: 42rem; margin-left: auto; margin-right: auto; padding: 1.5rem;   
Centered container

.classes('flex items-center gap-4')             
display: flex; align-items: center; gap: 1rem;   
Horizontal align with gap
"""


class ButtonDashboard:
    def __init__(self):
        self.button_press_count = {i: 0 for i in range(1, 7)}
        self.create_app()

    def create_app(self):
        # Header
        ui.label('Button Dashboard App').classes('text-2xl font-bold text-center w-full mt-4')

        # Status display area
        with ui.card().classes('w-full p-4 bg-blue-50'):
            ui.label('Status Display').classes('text-lg font-bold mb-2')
            self.status_label = ui.label('No button pressed yet').classes('text-lg p-2 bg-white rounded')
            self.count_label = ui.label('Press counts: ' + ', '.join([f'B{i}:0' for i in range(1, 7)])).classes(
                'text-sm text-gray-600')

        # Configuration section
        with ui.card().classes('w-full p-4 bg-gray-50'):
            ui.label('Button Configuration').classes('text-lg font-bold mb-4')

            with ui.grid(columns=2).classes('w-full gap-4'):
                self.text_input = ui.input(
                    label='Custom Button Text',
                    placeholder='Text to show in status'
                ).classes('w-full')

                self.color_input = ui.input(
                    label='Status Color Theme',
                    placeholder='color name (blue, green, etc)'
                ).classes('w-full')

                self.size_select = ui.select(
                    label='Button Size',
                    options=['small', 'medium', 'large'],
                    value='medium'
                ).classes('w-full')

        # Buttons in 3 rows
        with ui.card().classes('w-full p-4'):
            ui.label('Button Grid').classes('text-lg font-bold mb-4')

            # Row 1
            with ui.row().classes('w-full justify-center items-center gap-6 p-2'):
                ui.label('Actions:').classes('font-bold w-20')
                self.create_button(1, 'Primary Action', 'blue')
                self.create_button(2, 'Secondary Action', 'green')

            # Row 2
            with ui.row().classes('w-full justify-center items-center gap-6 p-2'):
                ui.label('Tools:').classes('font-bold w-20')
                self.create_button(3, 'Save', 'red')
                self.create_button(4, 'Load', 'yellow')

            # Row 3  
            with ui.row().classes('w-full justify-center items-center gap-6 p-2'):
                ui.label('Utils:').classes('font-bold w-20')
                self.create_button(5, 'Export', 'purple')
                self.create_button(6, 'Import', 'orange')

        # Control panel
        with ui.card().classes('w-full p-4 bg-green-50'):
            ui.label('Control Panel').classes('text-lg font-bold mb-4')

            with ui.row().classes('w-full justify-center gap-4'):
                ui.button('Clear All', on_click=self.clear_all).classes('bg-red-500 text-white')
                ui.button('Reset Counts', on_click=self.reset_counts).classes('bg-yellow-500 text-white')
                ui.button('Show Summary', on_click=self.show_summary).classes('bg-blue-500 text-white')

    def create_button(self, number: int, default_text: str, color: str):
        """Create a button with consistent styling"""
        color_classes = {
            'blue': 'bg-blue-500 hover:bg-blue-600',
            'green': 'bg-green-500 hover:bg-green-600',
            'red': 'bg-red-500 hover:bg-red-600',
            'yellow': 'bg-yellow-500 hover:bg-yellow-600',
            'purple': 'bg-purple-500 hover:bg-purple-600',
            'orange': 'bg-orange-500 hover:bg-orange-600'
        }

        size_classes = {
            'small': 'px-3 py-1 text-sm',
            'medium': 'px-4 py-2',
            'large': 'px-6 py-3 text-lg'
        }

        button_class = f"{color_classes[color]} text-white rounded {size_classes[self.size_select.value]}"

        return ui.button(
            default_text,
            on_click=lambda: self.handle_button_click(number, default_text)
        ).classes(button_class)

    def handle_button_click(self, button_number: int, default_text: str):
        """Handle button click and update status"""
        self.button_press_count[button_number] += 1

        # Get custom text from input
        custom_text = self.text_input.value
        display_text = f"{custom_text} " if custom_text else f"{default_text} "

        # Get color theme
        color_theme = f"({self.color_input.value})" if self.color_input.value else ""

        # Update status
        self.status_label.set_text(
            f'Button {button_number} pressed: {display_text}{color_theme} '
            f'(Total: {self.button_press_count[button_number]} times)'
        )

        # Update counts display
        counts_text = ', '.join([f'B{i}:{self.button_press_count[i]}' for i in range(1, 7)])
        self.count_label.set_text(f'Press counts: {counts_text}')

    def clear_all(self):
        """Clear all inputs and status"""
        self.status_label.set_text('All cleared! Ready for new actions.')
        self.text_input.set_value('')
        self.color_input.set_value('')

    def reset_counts(self):
        """Reset all button press counts"""
        self.button_press_count = {i: 0 for i in range(1, 7)}
        self.count_label.set_text('Press counts: ' + ', '.join([f'B{i}:0' for i in range(1, 7)]))
        self.status_label.set_text('All counts reset to zero!')

    def show_summary(self):
        """Show summary of all button presses"""
        total_presses = sum(self.button_press_count.values())
        most_used = max(self.button_press_count.items(), key=lambda x: x[1])

        summary = (
            f"Summary: {total_presses} total presses | "
            f"Most used: Button {most_used[0]} ({most_used[1]} times)"
        )
        self.status_label.set_text(summary)


if __name__ in {"__main__", "__mp_main__"}:
    dashboard = ButtonDashboard()
    ui.run(title="Advanced Button Dashboard", port=8080, reload=False)
