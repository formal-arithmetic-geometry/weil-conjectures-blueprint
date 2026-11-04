+++
id = "definition-kunneth-map"
kind = "definition"
title = "Künneth map"
order = 703
+++
Let $f_i:X_i\to Y_i$, $i=1,2$, be morphisms of separated $k$-schemes of
finite type, put $h=f_1\times f_2:X_1\times X_2\to Y_1\times Y_2$, and let
$M_i\in D^b_{\mathrm{ctf}}(X_i,A)$. The *Künneth map*

$$
Rf_{1*}M_1\boxtimes Rf_{2*}M_2
\longrightarrow Rh_*(M_1\boxtimes M_2)
\tag{8.3}
$$

is the adjoint transpose, for $h^*\dashv Rh_*$, of the morphism

$$
h^*(Rf_{1*}M_1\boxtimes Rf_{2*}M_2)
\simeq f_1^*Rf_{1*}M_1\boxtimes f_2^*Rf_{2*}M_2
\xrightarrow{\ \varepsilon_{f_1}\boxtimes\varepsilon_{f_2}\ }
M_1\boxtimes M_2,
$$

where $\varepsilon_{f_i}$ is the counit of $f_i^*\dashv Rf_{i*}$ and the first
isomorphism comes from $h^*p_i^*\simeq p_i^*f_i^*$.
