+++
id = "def-trf-supported-pairing"
kind = "definition"
title = "The supported pairing recipe"
order = 2436
uses = ["def-trf-correspondence", "def-trf-dualizing-complex", "def-trf-integration", "def-trf-local-term"]
+++
Let $X$ be a separated finite-type scheme with the dualizing data of
[def-trf-dualizing-complex], and let
$(C,c,u)$, $(D,d,v)$ be an *opposite pair* of
cohomological
correspondences on $X$ with $K\in D^b_{ctf}(X,A)$, in the notation of
[def-trf-correspondence]. Compose with
$\widetilde u\otimes\widetilde v$, then with the two Verdier
evaluations and the product comparison
$\omega_Y\boxtimes_A^{\mathrm L}\omega_X\simeq\omega_Z$. The
exceptional adjoint of this composite is the *Borel–Moore section*

$$
\langle u,v\rangle_{\mathrm{LV}}:A_E\longrightarrow\omega_E
$$

of [def-trf-integration]. For $v=1_K$ on the
diagonal, write $\Tr_c(u)=\langle u,1_K\rangle_{\mathrm{LV}}$ on
$\Fix(c)$, and abbreviate $\LT_B(u,v)=\LT_B(\langle u,v\rangle_{\mathrm{LV}})$
and $\LT_B(u)=\LT_B(\Tr_c(u))$, the local term of
[def-trf-local-term].
