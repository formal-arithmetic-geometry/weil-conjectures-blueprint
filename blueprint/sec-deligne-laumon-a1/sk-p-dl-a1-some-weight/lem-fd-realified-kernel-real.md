+++
id = "lem-fd-realified-kernel-real"
kind = "lemma"
title = "The realified kernel is $\\iota$-real"
order = 3078
uses = ["def-fd-kernel", "def-fd-nonexceptional", "def-fd-transform", "def-weil-pbc-constructible-complexes", "def-weil-punctual-weights", "def-wf-constant-weil-twist", "def-wf-fundamental-representation", "def-wf-iota-real", "def-wf-middle-extension", "lem-fd-as-characters", "lem-fd-as-lisse", "lem-fd-as-purity", "lem-trf-frobenius-degree-formula", "lem-wf-pure-realizable", "prop-kernel-lisse"]
+++
Let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$ be a dense open immersion with
$U_0=\mathbf A^1_{k_0}\setminus S_0$, and let $\mathcal M$ be an
irreducible lisse Weil
sheaf on $U_0$, unramified at infinity,
punctually $\iota$-pure of weight
$w$, with irreducible geometric fundamental representation of
[def-wf-fundamental-representation] and
middle extension that is
Fourier-nonexceptional. Put

$$
b:=\iota^{-1}(q^w),\qquad\text{so that}\qquad \iota(b)=q^w ,
\qquad
\mathcal M^\dagger:=\mathcal M^\vee\otimes\mathcal B_b ,
$$

the linear dual twisted by the constant
Weil twist, and let

$$
\mathcal K:=p_1^*(j_!\mathcal M)\otimes^L\mathcal K_\psi
\;\oplus\;
p_1^*\bigl(j_!(\mathcal M^\dagger)\bigr)\otimes^L\mathcal K_{\psi^{-1}}
$$

be the *realified kernel* on the Fourier square, the projections and
the Fourier kernel being those of
[def-fd-kernel] and the transform normalizations those of
[def-fd-transform]. Then $\mathcal K$ is
$\iota$-real in the sense of
[def-wf-iota-real]. More generally, the same conclusion holds, with
$b$, $\mathcal M^\dagger$ and $\mathcal K$ formed in the same way, for
*every* lisse Weil sheaf $\mathcal M$ on $U_0$ which is punctually
$\iota$-pure of weight $w$: the irreducibility, unramifiedness and
nonexceptionality hypotheses are not needed for the reality of the kernel.
