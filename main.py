import EncounterComposition
import FilePrinter
import StatblockGenerator

## Kinda pointless, but calls functions in the right order.
FilePrinter.PrintStatblocks(StatblockGenerator.GenerateStatblocks(EncounterComposition.GatherEncounterInfo()))