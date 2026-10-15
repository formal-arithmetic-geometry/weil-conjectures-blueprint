+++
id = "det-nagata-density-normalization-sheaves"
kind = "lemma"
title = "Extension by zero through the schematic closure"
uses = ["det-nagata-density-normalization-setup", "sk-prop-sf-open-closed-triangle"]
+++
In the situation of [det-nagata-density-normalization-setup], let
$\Lambda$ be a condensed coefficient ring with pulled-back coefficient
sheaves $\Lambda_X,\Lambda_Z,\Lambda_{\overline X}$. For every sheaf $M$ of
$\Lambda_X$-modules on $X_{\mathrm{pro\acute{e}t}}$ the unit
$\eta:j_!M\to i_*i^*j_!M$ of $i^*\dashv i_*$ is an isomorphism, and the
base-change isomorphism $i^*j_!M\simeq j_{Z,!}M$ identifies it with a natural
isomorphism

$$
j_!M\xrightarrow{\ \sim\ }i_*j_{Z,!}M .
$$

Consequently, for every complex $K$ of $\Lambda_X$-modules (unbounded), the
same map, applied degreewise, is an isomorphism of complexes
$j_!K\simeq i_*j_{Z,!}K$, and it induces the identification
$j_!K\simeq i_*j_{Z,!}K$ in $D(\overline X_{\mathrm{pro\acute{e}t}},\Lambda_{\overline X})$.
