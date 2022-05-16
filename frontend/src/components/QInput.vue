<script setup lang="ts">
const input = ref<HTMLInputElement>();

interface Props {
    type?: string;
    placeholder?: string;
    modelValue?: string;
    disabled?: boolean;
}

const props = withDefaults(defineProps<Props>(), {
    type: "text",
    placeholder: "",
    modelValue: "",
    disabled: false,
});

const emit = defineEmits(["update:modelValue"]);
function emitValue(inputValue: string): void {
    props.type === "tel" ? emit("update:modelValue", maskToTel(inputValue)) : emit("update:modelValue", inputValue);
}

function maskToTel(inputValue: string): string {
    if (input.value) {
      const isLastInputValueDigit = !/[^0-9]/g.test((input.value as any).value.at(-1));
      const isAddingSymbol = props.modelValue < input.value.value;
      if (isAddingSymbol) {
        if (isLastInputValueDigit) {
          const x = inputValue.replace(/[^\d]/g, "").match(/(\d{0,1})(\d{0,3})(\d{0,3})(\d{0,2})(\d{0,2})/);
          if (x) {
            return !x[3] ? `+7 (${x[2]}` : `+7 (${x[2]}) ${x[3]}` + (x[4] ? `-${x[4]}` : "") + (x[5] ? `-${x[5]}` : "");
          } else {
            return "";
          }
        } else {
          input.value.value = props.modelValue;
          return input.value.value;
        }
      } else {
        input.value.value = props.modelValue;
        return input.value.value.slice(0, -1);
      }
    } else return "";
  }


const fieldType = "QInput";
defineExpose({ fieldType });
</script>

<template>
    <input 
        :placeholder="props.placeholder" 
        :type="props.type || 'text'"
        :value="props.modelValue"
        @input="emitValue(($event.target as HTMLInputElement).value)"
        :maxlength="props.type === 'tel' ? '18' : ''"
        :disabled="props.disabled"
        autocomplete="false" ref="input"
        class="border-1 border-[#ffdd2d] py-5px bg-white text-left rounded outline-none active:outline-none px-4" text="12px md:14px"
    />
</template>
