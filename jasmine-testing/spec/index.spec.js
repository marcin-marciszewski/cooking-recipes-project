describe('index.html', function() {
    beforeEach(function() {
        jasmine.getFixtures().fixturesPath = '/project/templates/';
        loadFixtures('index.html');
    });

    describe('Buttons', function() {
        it("should open 'All recipes' page", function() {
            expect($('#allrecipes-button')).toBeInDOM()
            var spyEvent = spyOnEvent('#allrecipes-button', 'click');
            $('#allrecipes-button').click();
            expect('click').toHaveBeenTriggeredOn('#allrecipes-button');
            expect(spyEvent).toHaveBeenTriggered();
        });

        it("should open 'Add recipe' page", function() {
            expect($('#addrecipe-button')).toBeInDOM()
            var spyEvent = spyOnEvent('#addrecipe-button', 'click');
            $('#addrecipe-button').click();
            expect('click').toHaveBeenTriggeredOn('#addrecipe-button');
            expect(spyEvent).toHaveBeenTriggered();
        });

        it("should open 'Manage cuisines' page", function() {
            expect($('#managecuisines-button')).toBeInDOM()
            var spyEvent = spyOnEvent('#managecuisines-button', 'click');
            $('#managecuisines-button').click();
            expect('click').toHaveBeenTriggeredOn('#managecuisines-button');
            expect(spyEvent).toHaveBeenTriggered();
        });

        it("should open 'Statistics' page", function() {
            expect($('#statistics-button')).toBeInDOM()
            var spyEvent = spyOnEvent('#statistics-button', 'click');
            $('#statistics-button').click();
            expect('click').toHaveBeenTriggeredOn('#statistics-button');
            expect(spyEvent).toHaveBeenTriggered();
        });

        describe('Navbar', function() {
            it('should contain all classes for navbar', function() {
                expect($('.navbar-toggler')).toBeInDOM();
            });

            it('should open the droppind menu', function() {
                var spyEvent = spyOnEvent('.navbar-toggler', 'click');
                $('.navbar-toggler').click();
                expect('click').toHaveBeenTriggeredOn('.navbar-toggler');
                expect(spyEvent).toHaveBeenTriggered();
            });

            it('should contain 3 items in the carousel', function() {
                expect($('ol > li')).toHaveLength(3);
                expect($('<h2 class="display-3">Add a new recipe</h2>')).toContainText('Add a new recipe')
                expect($('<h2 class="display-3">Create your own cooking book</h2>')).toContainText('Create your own cooking book')
                expect($('<h2 class="display-3">Share your recipes with friends</h2>')).toContainText('Share your recipes with friends')
            });
        });

        describe('Main body', function() {
            it('should contain about section', function() {
                expect($('#about')).toBeInDOM();
                expect($('<h2>Recipes manager</h2>')).toContainText('Recipes manager')

            });
            it('should contain about cuisine', function() {
                expect($('#cuisines')).toBeInDOM();
                expect($('<h2>Cuisines</h2>')).toContainText('Cuisines')

            });
            it('should contain about contact', function() {
                expect($('#contact')).toBeInDOM();
                expect($('<div class="d-block">Send a message to us</div>')).toContainText('Send a message to us')

            });
        });
    });
});
