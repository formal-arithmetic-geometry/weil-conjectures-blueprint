+++
id = "definition-trace-class-local-terms"
kind = "definition"
title = "Trace class and local terms"
order = 917
+++
Let $u:c_2^*K\to c_1^!K$ be a cohomological correspondence on $(X,K)$.
By adjunction, $u$ is a section $A_C\to\mathcal H_c(K)$.
Its composite with the trace morphism of
Definition [definition-trace-morphism], transposed by $i_c^*\dashv Ri_{c*}$,
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
