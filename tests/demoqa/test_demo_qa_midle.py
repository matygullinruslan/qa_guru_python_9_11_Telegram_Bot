import allure
from selene import browser

from page.registration_page_midle import registration_page


def test_registration_demo_qa_midl():
    with allure.step('Открываем страницу регистрации'):
        registration_page.open()

    with allure.step('Изменяем масштаб страницы'):
        browser.driver.execute_script("document.querySelector('.body-height').style.transform='scale(.65)'")

    with allure.step('Принимаем соглашение'):
        browser.element('[aria-label="Consent"]').click()

    with allure.step('Заполняем форму регистрации'):
        registration_page.fill_last_name('Matygullin')
        registration_page.fill_name('Ruslan')
        registration_page.fill_email('ruslan@mail.ru')
        registration_page.fill_gender()
        registration_page.fill_phone('9770001010')
        registration_page.fill_date('21', 'February', '1992')
        registration_page.fill_subjects('Biology')
        registration_page.fill_state()
        registration_page.fill_hobbies()
        registration_page.fill_upload_file('rus.jpg')
        registration_page.fill_address('Ulyanovsk')
        registration_page.fill_city()

    with allure.step('Отправляем форму'):
        registration_page.fill_submit()

    with allure.step('Проверяем, что пользователь зарегистрирован'):
        registration_page.should_registered_user_with(
            'Ruslan Matygullin',
            'ruslan@mail.ru',
            'Male',
            '9770001010',
            '21 February,1992',
            'Biology',
            'Sports',
            'rus.jpg',
            'Ulyanovsk',
            'NCR Gurgaon',
        )
