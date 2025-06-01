<div align="left" style="position: relative;">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="right" width="30%" style="margin: -20px 0 0 20px;">
<h1>TRADEMARKET_DJANGO</h1>
<p align="left">
	<em><code>
		❯ Хочешь обновить свои вещи без лишних затрат? Присоединяйся к TradeMarket — платформе, где ты можешь легко обмениваться товарами с другими! Размещай свои объявления, находи крутые предложения и договаривайся об обмене в пару кликов. Удобный поиск, яркий дизайн и мгновенные уведомления сделают процесс увлекательным и простым. Начни обмениваться уже сегодня — твоя следующая находка ждёт тебя на TradeMarket! 🚀
	</code></em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/InomjonQurbonov/TradeMarket_Django?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/InomjonQurbonov/TradeMarket_Django?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/InomjonQurbonov/TradeMarket_Django?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/InomjonQurbonov/TradeMarket_Django?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="left"><!-- default option, no dependency badges. -->
</p>
<p align="left">
	<!-- default option, no dependency badges. -->
</p>
</div>
<br clear="right">

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

<code>❯
TradeMarket — это инновационная веб-платформа, созданная для удобного и безопасного обмена товарами между пользователями. Построенная на Django, она предоставляет интуитивно понятный интерфейс, где каждый может размещать объявления о своих товарах, предлагать обмен на другие объявления и управлять процессом сделки. Система уведомлений и email-оповещений держит пользователей в курсе всех новых предложений и изменений статуса. TradeMarket объединяет людей, которые хотят обмениваться вещами без лишних затрат, делая процесс обмена простым, прозрачным и увлекательным. Благодаря гибкой фильтрации по категориям и состоянию товаров, а также поддержке изображений, платформа идеально подходит как для личного использования, так и для сообществ, ценящих экологичный подход к потреблению.
</code>

---

## 👾 Features

<code>❯
1 . Публикация объявлений:
Пользователи могут создавать объявления с заголовком, описанием, изображением, категорией и состоянием товара (новое, б/у, старое).
Простая форма с автоматической загрузкой данных и валидацией.
2 . Предложения обмена:
Любой авторизованный пользователь может предложить обмен, создав своё объявление, связанное с целевым.
Владелец объявления может принять или отклонить предложение одним кликом.
3 . Система уведомлений:
Автоматические уведомления о новых предложениях обмена отображаются на главной странице.
Email-оповещения отправляются владельцам объявлений о поступивших предложениях.
Уведомления помечаются как прочитанные при просмотре объявления.
4 . Управление сделками:
При принятии предложения оба объявления (основное и предложенное) деактивируются для предотвращения дальнейших сделок.
При отклонении деактивируется только предложение обмена.
Уведомления отправляются отправителю предложения о решении.
5 . Фильтрация и поиск:
Удобная форма для поиска объявлений по названию, категории и состоянию.
Пагинация для навигации по большому списку товаров.
6 . Безопасность и доступ:
Требуется авторизация для создания объявлений и отправки предложений.
Проверка прав доступа для управления предложениями (опционально, в зависимости от настроек).
7 . Интуитивный интерфейс:
Аниме-стиль дизайна с яркими цветами и дружелюбными сообщениями.
Поддержка медиафайлов для отображения изображений товаров.
8 . Администрирование:
Панель администратора для управления пользователями, объявлениями и уведомлениями.
Лёгкая настройка через Django Admin.
</code>

---

## 📁 Project Structure

```sh
└── TradeMarket_Django/
    ├── LICENSE
    ├── README.md
    ├── app_ads
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── migrations
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── config
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    ├── media
    │   └── adsImage
    ├── requirements.txt
    └── templates
        ├── app_ads
        └── registration
```


### 📂 Project Index
<details open>
	<summary><b><code>TRADEMARKET_DJANGO/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/manage.py'>manage.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- templates Submodule -->
		<summary><b>templates</b></summary>
		<blockquote>
			<details>
				<summary><b>registration</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/templates/registration/register.html'>register.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/templates/registration/login.html'>login.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/templates/registration/base.html'>base.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/templates/registration/logout.html'>logout.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>app_ads</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/templates/app_ads/advertiser_form.html'>advertiser_form.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/templates/app_ads/swap_offer_form.html'>swap_offer_form.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/templates/app_ads/swap_offer_update.html'>swap_offer_update.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/templates/app_ads/advertiser_detail.html'>advertiser_detail.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/templates/app_ads/advertiser_confirm_delete.html'>advertiser_confirm_delete.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/templates/app_ads/base.html'>base.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/templates/app_ads/advertiser_list.html'>advertiser_list.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- config Submodule -->
		<summary><b>config</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/config/settings.py'>settings.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/config/urls.py'>urls.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/config/asgi.py'>asgi.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/config/wsgi.py'>wsgi.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- app_ads Submodule -->
		<summary><b>app_ads</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/app_ads/tests.py'>tests.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/app_ads/forms.py'>forms.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/app_ads/views.py'>views.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/app_ads/apps.py'>apps.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/app_ads/urls.py'>urls.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/app_ads/admin.py'>admin.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/app_ads/models.py'>models.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
			<details>
				<summary><b>migrations</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/app_ads/migrations/0003_notification.py'>0003_notification.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/app_ads/migrations/0001_initial.py'>0001_initial.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/InomjonQurbonov/TradeMarket_Django/blob/master/app_ads/migrations/0002_advertiser_target_ad.py'>0002_advertiser_target_ad.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with TradeMarket_Django, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


### ⚙️ Installation

Install TradeMarket_Django using one of the following methods:

**Build from source:**

1. Clone the TradeMarket_Django repository:
```sh
❯ git clone https://github.com/InomjonQurbonov/TradeMarket_Django
```

2. Navigate to the project directory:
```sh
❯ cd TradeMarket_Django
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```




### 🤖 Usage
Run TradeMarket_Django using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python manage.py makemigrations
❯ python manage.py migrate
❯ python manage.py runserver
```



---
## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Preparing the database.</strike>
- [X] **`Task 2`**: Setting up the first settings.
- [X] **`Task 3`**: Development of a project registration system.
- [X] **`Task 4`**: Creating and manually testing models.
- [X] **`Task 5`**: Preparing 80% of the project (adding and testing filters, search and API systems.
- [ ] **`Task 3`**: Putting it on the server and running it.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/InomjonQurbonov/TradeMarket_Django/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/InomjonQurbonov/TradeMarket_Django/issues)**: Submit bugs found or log feature requests for the `TradeMarket_Django` project.
- **💡 [Submit Pull Requests](https://github.com/InomjonQurbonov/TradeMarket_Django/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/InomjonQurbonov/TradeMarket_Django
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/InomjonQurbonov/TradeMarket_Django/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=InomjonQurbonov/TradeMarket_Django">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [SELECT-A-LICENSE](https://github.com/InomjonQurbonov/TradeMarket_Django?tab=MIT-1-ov-file#readme) License. For more details, refer to the [LICENSE](https://github.com/InomjonQurbonov/TradeMarket_Django?tab=MIT-1-ov-file#readme) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
