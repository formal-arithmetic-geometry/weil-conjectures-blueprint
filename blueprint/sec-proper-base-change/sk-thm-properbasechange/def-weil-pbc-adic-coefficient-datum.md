+++
id = "def-weil-pbc-adic-coefficient-datum"
kind = "definition"
title = "Tower category and adic coefficient datum"
order = 1306
uses = ["def-weil-pbc-kinjective-resolutions", "def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-operations", "def-weil-pbc-proetale-site"]
+++
For a sheaf of rings $B_T$ on $T_{\Proet}$, define the Grothendieck abelian
category

$$
 \operatorname{Tow}_{B}(T)=
 \operatorname{Fun}\bigl(\mathbf N_{\geq1}^{\mathrm{op}},
              \Mod(T_{\Proet},B_T)\bigr).
$$

Its objects are strict inverse sequences $M_1\leftarrow M_2\leftarrow\cdots$,
and kernels, cokernels, and exactness are computed levelwise. Write
$\operatorname{ev}_n:\operatorname{Tow}_{B}(T)\to\Mod(T_{\Proet},B_T)$ for
the exact evaluation functor.

Let $A$ be noetherian, let $I=(a_1,\dots,a_r)$, assume $A/I$ is torsion, and
put $P_n=A/I^n$. Give $P_n$ the discrete topology and let $(P_n)_T$ be the
sheafification of

$$
 U\longmapsto\operatorname{Cont}(\pi_0(|U|),P_n)
$$

on $T_{\Proet}$. Define

$$
 A_T=\varprojlim_n(P_n)_T,
 \qquad
 D(T_{\Proet},A)=D(\Mod(T_{\Proet},A_T)),
$$

and assume each $P_n$ is finite as a set and perfect as an $A$-module. For
$K\in D(T_{\Proet},A)$ choose a functorial K-flat representative $QK$ (in the
sense of [def-weil-pbc-proetale-operations]). The strict complexes

$$
 QK\otimes_{A_T}(P_n)_T
$$

and the quotient maps $P_{n+1}\to P_n$ define an object $K_\bullet\in
D(\operatorname{Tow}_{A}(T))$. Its $n$-th evaluation is canonically

$$
 K_n=K\otimes^L_{A_T}(P_n)_T,
$$

and it carries functorial normalization isomorphisms

$$
 K_{n+1}\otimes^L_{P_{n+1}}P_n\xrightarrow{\sim}K_n
$$

satisfying the quotient cocycle.
