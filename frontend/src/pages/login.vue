<script setup lang="ts">
const store = useStore()
</script>

<template>
    <div w-screen h-screen flex flex-col bg="[#ffffff]">
        <header>
            <div absolute left="20px xl:50px" top="10px xl:30px">
                <p text="32px" fw-700>ToDo List</p>
                <h1 text="[#4d4d4d] 14px" fw-500>crossplatform</h1>
            </div>
        </header>
        <main fixed left-10px right-10px top-10px bottom="50px xl:43px">
            <section h-full w-full flex items-center justify-center>
                <div flex relative h-450px w="full xl:720px" my-20px border="xl:1px [#e1e3e6]" rounded-10px
                    overflow-hidden>
                    <div class="w-full lg:w-360px h-full flex-grow-0 flex-shrink-0 box-border p-28px pb-16px">
                        <img mt="40px xl:0" mb-20px mx-auto z-99999
                            src="https://yastatic.net/s3/frontend/tutor/_/cover-8ada143dd5.svg" alt="" width="136"
                            height="auto">
                        <p text="16px xl:20px" fw-600>Войдите или зарегистрируйтесь</p>
                        <div my-10px>По логину и паролю</div>
                        
                        <QInput v-model="store.login" my-10px w-full placeholder="Введите логин"></QInput>
                        <QInput v-model="store.password" my-10px w-full placeholder="Введите пароль"></QInput>

                        <NuxtLink mt-10px to="/todo">
                            <QButton w-full>
                                Продолжить
                            </QButton>
                        </NuxtLink>
                        
                    </div>
                </div>
            </section>
        </main>
        <footer fixed bottom-0 left-0 right-0 h="40px xl:33px" border="t [#e7e7e7]">
            <div w="full xl:1024px" h-full mx-auto p="x-20px xl:0">
                <div mt="5px xl:0" w-full h-full grid grid-cols="[1fr_1fr] xl:[2fr_1fr_1fr]"
                    grid-rows="[10px_10px] xl:[1fr]" gap="5px xl:0" text="xl:center" items-center>
                    <QLink col-span="2 xl:1" text="10px xl:12px">Вадим Лукин ПИ-2-18</QLink>
                    <QLink text="10px xl:12px">Nuxt + capacitorjs</QLink>
                    <QLink text="10px xl:12px">ionic (Hybrid Web)</QLink>
                </div>
            </div>
        </footer>
    </div>
</template>