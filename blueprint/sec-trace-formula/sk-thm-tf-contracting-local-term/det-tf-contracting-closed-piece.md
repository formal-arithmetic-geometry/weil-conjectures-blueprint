+++
id = "det-tf-contracting-closed-piece"
kind = "lemma"
title = "The trace class is carried by the closed piece"
order = 3801
uses = ["det-tf-contracting-restricted-morphism", "det-tf-contracting-vanishing", "det-tf-fixed-ideal-nilpotent", "prop-trf-trace-class-additivity", "thm-trf-trace-proper-compatibility"]
+++
In the setting of [det-tf-contracting-vanishing], drop the hypothesis $i^*K=0$, and let
$c_Z:C_Z\to Z_{\mathrm{red}}\times Z_{\mathrm{red}}$ and
$u_Z:c_{Z,2}^*i^*K\to c_{Z,1}^!i^*K$ be the restricted correspondence and morphism of
[det-tf-contracting-restricted-morphism]. Let $h:F_{c_Z}\to F_c$ be the induced map of fixed
schemes. Then $h$ is an isomorphism after reduction, and

$$
 \operatorname{Tr}_c(u)=h_*\operatorname{Tr}_{c_Z}(u_Z).
$$

If $F_c$ is proper, the local terms of $u$ and of $u_Z$ are equal.
