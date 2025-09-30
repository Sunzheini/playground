from nicegui import ui


# tailwind classes:
"""
# Width
.classes('w-full')        # 100% width
.classes('w-1/2')         # 50% width  
.classes('w-1/3')         # 33% width
.classes('w-64')          # 256px width
.classes('w-auto')        # auto width
.classes('max-w-md')      # max-width: 28rem (448px)
.classes('max-w-lg')      # max-width: 32rem (512px)

# Height
.classes('h-screen')      # 100vh height
.classes('h-full')        # 100% height
.classes('h-64')          # 256px height

.classes('p-2')           # 8px padding
.classes('p-4')           # 16px padding (most common)
.classes('p-6')           # 24px padding
.classes('px-4')          # 16px left/right
.classes('py-2')          # 8px top/bottom
.classes('pt-4')          # 16px top only
.classes('pb-2')          # 8px bottom only

.classes('m-2')           # 8px margin
.classes('m-4')           # 16px margin
.classes('mx-auto')       # center horizontally
.classes('my-4')          # 16px top/bottom margin
.classes('mt-2')          # 8px top margin
.classes('mb-4')          # 16px bottom margin

.classes('gap-2')         # 8px gap (small)
.classes('gap-4')         # 16px gap (medium - most common)
.classes('gap-6')         # 24px gap (large)

# Primary colors
.classes('bg-blue-500')   # Medium blue
.classes('bg-green-500')  # Medium green
.classes('bg-red-500')    # Medium red
.classes('bg-yellow-500') # Medium yellow
.classes('bg-purple-500') # Medium purple
.classes('bg-gray-500')   # Medium gray

# Light backgrounds
.classes('bg-blue-50')    # Very light blue
.classes('bg-gray-50')    # Very light gray
.classes('bg-green-50')   # Very light green
.classes('bg-white')      # White
.classes('bg-transparent') # Transparent

# Text Colors
.classes('text-white')     # White text
.classes('text-black')     # Black text
.classes('text-gray-600')  # Dark gray text
.classes('text-gray-400')  # Light gray text
.classes('text-blue-600')  # Blue text
.classes('text-red-600')   # Red text

# Borders and Radius
.classes('border')         # 1px border
.classes('border-2')       # 2px border
.classes('border-gray-300') # Light gray border
.classes('border-blue-500') # Blue border
.classes('rounded')        # Small border radius
.classes('rounded-lg')     # Large border radius
.classes('rounded-full')   # Full rounded (circles)

# Text size
.classes('text-sm')        # Small text
.classes('text-base')      # Base text (default)
.classes('text-lg')        # Large text
.classes('text-xl')        # Extra large
.classes('text-2xl')       # 2x large
.classes('text-3xl')       # 3x large

# Font Weight
.classes('font-normal')    # Normal weight
.classes('font-medium')    # Medium weight
.classes('font-bold')      # Bold (most common)
.classes('font-semibold')  # Semi-bold

Text Alignment
.classes('text-left')      # Left align
.classes('text-center')    # Center align (common)
.classes('text-right')     # Right align

Flexbox
.classes('flex')           # Display flex
.classes('flex-col')       # Flex column
.classes('flex-row')       # Flex row (default)
.classes('items-center')   # Vertical center
.classes('items-start')    # Vertical start
.classes('justify-center') # Horizontal center
.classes('justify-between') # Space between
.classes('justify-around')  # Space around

# Grid
.classes('grid')           # Display grid
.classes('grid-cols-2')    # 2 columns
.classes('grid-cols-3')    # 3 columns
.classes('grid-cols-4')    # 4 columns

Shadows
.classes('shadow')         # Small shadow
.classes('shadow-md')      # Medium shadow
.classes('shadow-lg')      # Large shadow
.classes('shadow-none')    # No shadow

Hover Effects
.classes('hover:bg-blue-600')    # Darker blue on hover
.classes('hover:shadow-lg')      # Larger shadow on hover
.classes('hover:scale-105')      # Slight scale on hover

Opacity
.classes('opacity-50')     # 50% opacity
.classes('opacity-75')     # 75% opacity
.classes('opacity-100')    # 100% opacity (normal)

COMMON COMBINATIONS: Cards
.classes('p-4 bg-white rounded shadow')  # Basic card
.classes('p-6 bg-gray-50 rounded-lg border')  # Fancy card

# COMMON COMBINATIONS: Buttons
.classes('px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600')
.classes('px-3 py-1 bg-gray-200 text-gray-800 rounded')

# COMMON COMBINATIONS: Inputs
.classes('p-2 border rounded w-full')    # Full width input
.classes('px-3 py-2 border rounded')     # Standard input

# COMMON COMBINATIONS: Layouts
.classes('w-full p-4')                   # Full width section
.classes('max-w-2xl mx-auto p-6')        # Centered container
.classes('flex items-center gap-4')      # Horizontal align with gap


QUICK START RECIPES
# Header
.classes('text-2xl font-bold text-center p-4')

# Navigation row
.classes('flex gap-4 p-4 bg-gray-100')

# Content card  
.classes('p-6 bg-white rounded-lg shadow max-w-2xl mx-auto')

# Button primary
.classes('px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600')

# Button secondary
.classes('px-4 py-2 bg-gray-200 text-gray-800 rounded hover:bg-gray-300')

# Status message
.classes('p-3 bg-green-100 text-green-800 rounded')

# Error message  
.classes('p-3 bg-red-100 text-red-800 rounded')
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
