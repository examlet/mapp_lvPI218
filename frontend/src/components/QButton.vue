<script setup lang="ts">
const props = defineProps({ 
    disabled: { type: Boolean, required: false },
})

const emit = defineEmits(["click"]);
</script>

<template>
    <button
        class="inline-block rounded tracking-wide transition-all h-32px px-20px leading-32px items-center fw700"
        bg="[#ffdd2d] hover:[#fcc521] active:[#fab619]" text="12px [#222222]" fw-700
        :disabled="props.disabled" @click="emit('click')"
    >
        <slot />
    </button>
</template>