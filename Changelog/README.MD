# Releasenotes

## Version 26.11
 - Changes in helpstring documentation
 - Deprecated DbeJob.SetId() due to a bug
 - Added the following functions to Graph:
    - GetText
    - SetText
    - GetTextHeight
    - SetTextHeight
    - GetTextMode
    - SetTextMode
    - GetTextStyle
    - SetTextStyle
    - GetTextFontName
    - SetTextFontName
    - GetTextColour
    - SetTextColour
    - GetInternalText
 - Deprecated buggy functions in DbeJob: GetOutbarText, GetResultText
 - Added two missing types blob and mil line to the GraphType enum.

## Version 26.10
 - New function ProjectConfigurator.ChangeSignal (E3.2026 26.01, E3.2027 27.00)
 - Fix: In DbeSymbol.ImportDXF and DbeModel.ImportDXF the parameter flags was missing
 - Greatly enhanced helpstrings
 - New enum type ConfigFileType

## Version 0.5
 - New function Configurator.SwapSymbol (2026 26.01, 2027 27.00)
 - New functions AttributeDefinition.GetAttributeListValues and AttributeDefinition.GetValueListName (2025 25.34, 2026 26.01, 2027 27.00)
 - New function Slot.GetDefinedRotation (2026 26.01, 2027 27.00)
 - Fix: The functions SetCrimpingRules and GetCrimpingRules in DbeModelPin had a wong variable type
 - Fix: Type of the parameter additionalAttributes of DbeApplication.GetComponentList
 - New enum type GraphType
 - New enum type SymbolType
 - New enum type ComponentType
 - New enum type ComponentSubType 

## Version 0.4
- Added `language` to the `e3series.tools.StartArguments`.
- Fixed a bug in variant to dict conversion
- Fix: `e3series.tools.start()` modifies the args argument if a string list is provided and `wait_for_com` is True.
- Fix: `e3series.tools.start(keep_alive=False)` does not work if the script process is not already in a process-job.
- Fix: A bug lead to empty lists inside dictionaries
- Added treatment for dict [IN] parameters
- settings parameter of Device.GetTerminalPlanSettings() and Job.GetTerminalPlanSettings() actually is [IN/OUT], not [IN], corrected this in the library. The Documentation is currently wrong. Providing a non empty dict enables you to only get specified settings.
- Added the following enum types for usage with the AttributeDefinitionInterface: AD_Direction, AD_Owner, AD_Ratio, AD_Type, AD_UniqueValue

## Version 0.3
- Added `e3series.tools.E3seriesOutput` to redirect the output of the print function to the E3.series message window.

## Version 0.2
- First Release. Contains wrappers for all COM-Objects of the E3.series release 26.0.

## Version 0.1
- Placeholder package with no content.