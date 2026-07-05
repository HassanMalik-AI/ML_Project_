document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('predict-form');
    const resultContainer = document.getElementById('result-container');
    const submitBtn = document.getElementById('submit-btn');
    const btnText = submitBtn.querySelector('.btn-text');
    const spinner = submitBtn.querySelector('.spinner');
    const scoreElement = document.getElementById('predicted-score');
    const resetBtn = document.getElementById('reset-btn');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Show loading state
        btnText.classList.add('hidden');
        spinner.classList.remove('hidden');
        submitBtn.disabled = true;

        const formData = new FormData(form);

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                const errorData = await response.json();
                console.error("Server Error:", errorData);
                throw new Error(errorData.error || 'Network response was not ok');
            }

            const data = await response.json();
            
            // Hide form and show result
            form.classList.add('hidden');
            resultContainer.classList.remove('hidden');
            
            // Animate score counter
            animateScore(data.math_score);
            
        } catch (error) {
            console.error('Error:', error);
            alert('Prediction Failed: ' + error.message);
        } finally {
            // Reset button state
            btnText.classList.remove('hidden');
            spinner.classList.add('hidden');
            submitBtn.disabled = false;
        }
    });

    resetBtn.addEventListener('click', () => {
        form.reset();
        resultContainer.classList.add('hidden');
        form.classList.remove('hidden');
        scoreElement.textContent = '0';
    });

    function animateScore(targetScore) {
        let currentScore = 0;
        const duration = 1500; // 1.5 seconds
        const steps = 60;
        const increment = targetScore / steps;
        const stepTime = duration / steps;
        
        const timer = setInterval(() => {
            currentScore += increment;
            if (currentScore >= targetScore) {
                currentScore = targetScore;
                clearInterval(timer);
            }
            scoreElement.textContent = Math.round(currentScore);
        }, stepTime);
    }
});
