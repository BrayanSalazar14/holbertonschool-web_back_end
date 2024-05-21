import globals from "globals";
import pluginJs from "@eslint/js";

export { globals }; // Si necesitas exportar las globales por alguna razón específica
export default {
  languageOptions: { globals: { ...globals.browser, ...globals.node } },
  ...pluginJs.configs.recommended,
};