<script setup lang="ts">
interface TODOS {
    index: Number,
    login: String,
    uuid: String,
    name: String,
    description: String,
    checked: Boolean
}

const name = ref('');
const description = ref('');
const store = useStore()

const tds = ref<TODOS[]>([])

fetch(`https://gj5h6a.deta.dev/api/get`, {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({
            
        })
    })
        .then((res) => {
            if (!res.ok) {
                console.log('res not ok')
            } else {
                return res.json();
            }
        }).then((data) => {
            console.log(data)
            for(var i = 0; i < data.length; i++) {
                var obj = data[i];

                tds.value.push({
                    index: Date.now() + i,
                    login: obj['login'],
                    uuid: obj['uuid'],
                    name: obj['name'],
                    description: obj['description'],
                    checked: false
                })
            }
            tds.value = tds.value.filter(function (f) { return f.login == store.login })
        }).catch(e => console.log('Connection error', e));

const addTODO = () => {
    let date = Date.now();
    tds.value.push({
        index: date,
        login: store.login,
        uuid: String(Date.now()),
        name: name.value,
        description: description.value,
        checked: false
    })
    fetch(`https://gj5h6a.deta.dev/api/add`, {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({
            login: store.login,
            name: name.value,
            description: description.value,
        })
    })
        .then((res) => {
            if (!res.ok) {
                console.log('res not ok')
            } else {
                return res.json();
            }
        }).then((data) => {
            console.log('okay')
        }).catch(e => console.log('Connection error', e));
}

const removeTODO = (i) => {
    let old_tds = tds.value.filter(function (f) { return f.index == i })
    tds.value = tds.value.filter(function (f) { return f.index !== i })
    fetch(`https://gj5h6a.deta.dev/api/remove?uuid=${old_tds[0].uuid}`, {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({
            
        })
    })
        .then((res) => {
            if (!res.ok) {
                console.log('res not ok')
            } else {
                return res.json();
            }
        }).then((data) => {
            console.log('okay')
        }).catch(e => console.log('Connection error', e));
}
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
                        <p text="16px xl:20px" fw-600>Создайте или отметьте выполненное</p>
                        <QInput v-model="name" my-10px w-full placeholder="Введите название"></QInput>
                        <QInput v-model="description" my-10px w-full placeholder="Введите описание"></QInput>
                        <QButton @click="addTODO" w-full mb-30px>
                            Создать
                        </QButton>

                        <div v-for="(td, index) in tds" :key="index" gap="5px lg:0" grid
                            grid-cols="1 lg:[4fr_3fr_2fr_3fr_3fr]" items-center w-full h="lg:60px" mb-5px rounded
                            style="box-shadow: 0 10px 56px rgb(0 0 0 / 7%); border-left: 6px solid #0077ff;">
                            <div ml-20px mt="5px lg:0" fw-700>{{ td.name }}</div>
                            <div ml="20px lg:0">{{ td.description }}</div>
                            <QButton @click="removeTODO(td.index)" ml="20px" w="80%" mb="10px lg:0">ВЫПОЛНИТЬ</QButton>
                        </div>
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