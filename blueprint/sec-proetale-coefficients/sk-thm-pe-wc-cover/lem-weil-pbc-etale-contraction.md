+++
id = "lem-weil-pbc-etale-contraction"
kind = "lemma"
title = "Strict henselian local rings in the etale contraction"
order = 944
lean = ["indEtale_indEtaleContraction", "faithfullyFlat_indEtaleContraction", "RingHom.Etale.exists_comp_eq_id_indContraction", "IsStrictlyHenselianLocalRing.localization_atPrime_indEtaleContraction"]
uses = ["def-weil-pbc-etale-contraction", "def-weil-pbc-henselian-terminology", "def-weil-pbc-ind-etale-algebra", "lem-weil-pbc-etale-finite-data-descent", "lem-weil-pbc-ind-etale-stability"]
+++
The map $R\to R^{\mathrm e}$ is faithfully flat and ind-etale
[def-weil-pbc-ind-etale-algebra]. Every faithfully flat etale algebra of
finite presentation over $R^{\mathrm e}$ has a section. Every maximal
localization of $R^{\mathrm e}$ is strictly henselian
[def-weil-pbc-henselian-terminology].
