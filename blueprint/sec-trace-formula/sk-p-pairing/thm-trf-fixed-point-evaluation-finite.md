+++
id = "thm-trf-fixed-point-evaluation-finite"
kind = "theorem"
title = "Stalk traces on a finite etale fixed scheme"
order = 2661
uses = ["def-trf-categorical-trace", "def-trf-coefficient-conventions", "def-trf-fixed-scheme", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-finite-tor-amplitude", "def-weil-scheme-morphism-properties", "def-weil-site-perfect-complex", "lem-trf-chain-supertrace", "thm-trf-internal-hom-pullback"]
+++
Use the finite coefficient ring
$A=A_{E,n}$. Let $h:X\to X$ be an endomorphism of a
separated finite-type
$k$-scheme and let $K\in D^b_{ctf}(X,A)$ be a
site-perfect complex.
Suppose its fixed scheme
$j:F=\operatorname{Fix}(h)\to X$ is finite etale over $k$.
For the derived internal Hom
there is a natural morphism

$$
\sigma_{h,K}:Lj^*R\mathcal Hom_A(Lh^*K,K)\longrightarrow A_F.
$$

If $u:Lh^*K\to K$ has internal-Hom mate
$\widetilde u:A_X\to R\mathcal Hom_A(Lh^*K,K)$, the value at
$y\in F(k)$ of $\sigma_{h,K}\circ Lj^*\widetilde u$ is

$$
\operatorname{tr}_A(u_y\mid K_y),
$$

the categorical trace of the
endomorphism obtained from $hj=j$. This is a statement about stalk
traces; it does not identify them with Verdier local terms.
