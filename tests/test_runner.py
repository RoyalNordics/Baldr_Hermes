from core.hermes_core import process_task

task = """
Byg en React-komponent kaldet CustomButton.js.

🔧 Krav:
- Komponentnavn: CustomButton
- Props: 
  - label (tekst på knappen)
  - onClick (funktion der kaldes ved klik)
  - type (primary/secondary) som styrer farven
- Brug TailwindCSS til styling
- Returnér kun JSX-komponenten og afslut med: export default CustomButton;
"""

result = process_task(task)

print("=== Hermes Output ===\n")
print(result)
