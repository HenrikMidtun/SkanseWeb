
function reorderTableBody(table, entry_id)
{
    var entries = document.getElementsByClassName("table-entry");
    for(i=0; i< entries.length; i++)
    {
        entries[i].parentNode.insertBefore(entries[i],document.getElementById(entry_id));
    }

}
function onCompletedTask(e)
{
    var entry_id = e.parentNode.parentNode.id;
    var old_table = document.getElementById("tasks");
    reorderTableBody(old_table, entry_id);
}