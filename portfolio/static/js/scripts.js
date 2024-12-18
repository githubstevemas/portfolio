document.addEventListener('DOMContentLoaded', () => {
    const projects = Array.from(document.querySelectorAll('.repo-container'));
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const itemsPerPage = 4;
    let currentPage = 0;

    function updateProjectsDisplay() {
        projects.forEach((project, index) => {
            project.style.display = (index >= currentPage * itemsPerPage && index < (currentPage + 1) * itemsPerPage)
                ? 'block'
                : 'none';
        });

        prevBtn.disabled = currentPage === 0;
        nextBtn.disabled = currentPage >= Math.ceil(projects.length / itemsPerPage) - 1;
    }

    prevBtn.addEventListener('click', () => {
        if (currentPage > 0) {
            currentPage--;
            updateProjectsDisplay();
        }
    });

    nextBtn.addEventListener('click', () => {
        if (currentPage < Math.ceil(projects.length / itemsPerPage) - 1) {
            currentPage++;
            updateProjectsDisplay();
        }
    });

    updateProjectsDisplay();
});