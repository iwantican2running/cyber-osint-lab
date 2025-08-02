const terminalOutput = document.getElementById('terminal-output');
const cursor = document.createElement('span');
cursor.innerText = '|';
cursor.className = 'cursor';
terminalOutput.appendChild(cursor);

const commands = [
    "Initializing OSINT framework...",
    "Gathering data from sources...",
    "Analyzing information...",
    "Compiling results...",
    "OSINT report ready."
];

let commandIndex = 0;

function typeCommand(command) {
    return new Promise(resolve => {
        let index = 0;
        const typingInterval = setInterval(() => {
            terminalOutput.innerText += command[index++];
            if (index === command.length) {
                clearInterval(typingInterval);
                setTimeout(resolve, 500);
            }
        }, 100);
    });
}

async function simulateTerminalOutput() {
    for (const command of commands) {
        await typeCommand(command);
        terminalOutput.innerText += '\n';
    }
    cursor.style.display = 'none'; // Hide cursor after typing
}

setInterval(() => {
    cursor.style.visibility = (cursor.style.visibility === 'hidden' ? 'visible' : 'hidden');
}, 500);

document.getElementById('fetch-data-btn').addEventListener('click', () => {
    terminalOutput.innerText = ''; // Clear previous output
    commandIndex = 0; // Reset command index
    simulateTerminalOutput();
});

// Dynamic data visualization (example)
const dataVisualization = document.getElementById('data-visualization');

function updateVisualization() {
    dataVisualization.innerText = `Latest findings: ${Math.random().toFixed(2)}`; // Simulation with random data
}

setInterval(updateVisualization, 3000); // Update every 3 seconds
```

In this code, we simulate a terminal output with dynamic typing and blinking cursor effects while adding an interactive button to fetch data and update a simple data visualization section.