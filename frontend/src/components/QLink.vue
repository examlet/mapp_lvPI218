<script setup lang="ts">
const props = defineProps({
    primary: { type: Boolean, required: false },
    secondary: { type: Boolean, required: false },
    active: { type: Boolean, required: false },
    disabled: { type: Boolean, required: false },
})

const emit = defineEmits(["click"]);
</script>

<template>
    <div 
        cursor-pointer inline-flex flex-row text-14px tracking-wide transition-colors duration-300
        :disabled="disabled" @click="emit('click')"
    >
        <div v-if="props.primary" :class="{ 'underline': props.active }" fw-500 underline-offset-5 text="[#222222] active:[#9bdff7]" decoration="2px [#ffdd2d] hover:[#26bcf1] active:[#93dcf7]">
            <slot />
        </div>
        <div v-else-if="props.secondary" :class="{ 'underline': props.active }" fw-500 text="[#8a959b] hover:[#424951] active:[#26bcf1]">
            <slot />
        </div>
        <div v-else :class="{ 'underline': props.active }" fw400 text="[#8a959b] hover:[#121921]" decoration="dotted [#8a959b] hover:[#121921]" underline-offset-4>
            <slot />
        </div>
    </div>
</template>

<style scoped>
</style>