$(function() {
$("#number").append(list.length)
if (list.length == 0) {
$("#search_results").append("Sorry, there are no matching results")
}



for (let i = 0; i < list.length; i++) {
     let this_name = list[i];
     this_id = this_name.id
     name = this_name.name
     department = this_name.department
     year = this_name.year


        const highlightedName = name.replace(
                 new RegExp(query, 'gi'),
                 '<span class="highlight">$&</span>')
        name = highlightedName


        department = this_name.department

            const highlightedDepartment = department.replace(
                     new RegExp(query, 'gi'),
                     '<span class="highlight">$&</span>')
            department = highlightedDepartment

        year= this_name.year

                    const highlightedYear = year.replace(
                             new RegExp(query, 'gi'),
                             '<span class="highlight">$&</span>')
                    year = highlightedYear




     $("#search_results").append("<a data-id='" + this_name.id + "'href = 'view/" + this_name.id + "'> " + name+"-"+department +"("+year+") </a> <br>");
}




})