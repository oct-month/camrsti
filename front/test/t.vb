Sub ConvertWordsToPdfs()
    'Updated by Extendoffice 20181123
    Dim xIndex As String
    Dim xDlg As FileDialog
    Dim xFolder As Variant
    Dim xNewName As String
    Dim xFileName As String
    Set xDlg = Application.FileDialog(msoFileDialogFolderPicker)
    If xDlg.Show <> -1 Then Exit Sub
    xFolder = xDlg.SelectedItems(1) + "\"
    xFileName = Dir(xFolder & "*.*", vbNormal)
    While xFileName <> ""
        If ((Right(xFileName, 4)) <> ".doc" Or Right(xFileName, 4) <> ".docx") Then
            xIndex = InStr(xFileName, ".") + 1
            xNewName = Replace(xFileName, Mid(xFileName, xIndex), "pdf")
            Documents.Open FileName:=xFolder & xFileName, _
                ConfirmConversions:=False, ReadOnly:=False, AddToRecentFiles:=False, _
                PasswordDocument:="", PasswordTemplate:="", Revert:=False, _
                WritePasswordDocument:="", WritePasswordTemplate:="", Format:= _
                wdOpenFormatAuto, XMLTransform:=""
            ActiveDocument.ExportAsFixedFormat OutputFileName:=xFolder & xNewName, _
                ExportFormat:=wdExportFormatPDF, OpenAfterExport:=False, OptimizeFor:= _
                wdExportOptimizeForPrint, Range:=wdExportAllDocument, From:=1, To:=1, _
                Item:=wdExportDocumentContent, IncludeDocProps:=True, KeepIRM:=True, _
                CreateBookmarks:=wdExportCreateNoBookmarks, DocStructureTags:=True, _
                BitmapMissingFonts:=True, UseISO19005_1:=False
            ActiveDocument.Close
        End If
        xFileName = Dir()
    Wend
End Sub