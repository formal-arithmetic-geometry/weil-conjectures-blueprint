+++
id = "sk-d-trace-class"
kind = "definition"
title = "Trace class and local terms"
order = 557
uses = ["sk-d-corr", "sk-d-pairing", "sk-thm-sf-kunneth-verdier"]
tags = ["sketch"]
+++
Let $u:c_2^*K\to c_1^!K$ be a cohomological correspondence on $(X,K)$.
By adjunction, $u$ is a section $A_C\to\mathcal H_c(K)$.
Its composite with the trace morphism of
Lemma [sk-thm-sf-kunneth-verdier], transposed by $i_c^*\dashv Ri_{c*}$,
is the *trace class*

$$
\operatorname{Tr}_c(u):A_{\Fix(c)}\longrightarrow\omega_{\Fix(c)}.
$$

For a proper $k$-scheme $B$, integration is the counit map

$$
\int_B:H^0(B,\omega_B)
=H^0(Ra_{B!}a_B^!A_s)\longrightarrow A.
$$

If $B\subset \Fix(c)$ is proper and open and closed, the *local term*
of $u$ on $B$ is

$$
\operatorname{LT}_B(u)=\int_B\operatorname{Tr}_c(u)|_B.
$$

*Complement.* The trace class is also the supported pairing of $u$ against the
diagonal identity. For $(X,K)$, the diagonal identity is the
endocorrespondence with support $X$, support map $\Delta_X:X\to X\times X$,
identity legs, and coefficient map $1_K$; its intersection with $(C,c,u)$ is
$F_c=\Fix(c)$. The contraction of [sk-d-pairing], applied to the supported
classes $\widetilde u$ of $u$ and of $1_K$ and carried out over the Cartesian
square $F_c=C\times_{X\times X}X$, lands directly on $F_c$, and

$$
\Tr_c(u)=\langle u,1_K\rangle_{\mathrm{LV}}:A_{F_c}\longrightarrow\omega_{F_c}.
$$
