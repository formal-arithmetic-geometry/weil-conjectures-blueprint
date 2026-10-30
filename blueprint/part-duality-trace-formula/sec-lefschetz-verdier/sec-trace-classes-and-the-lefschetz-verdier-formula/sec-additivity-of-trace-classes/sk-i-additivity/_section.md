+++
id = "sk-i-additivity"
kind = "proposition"
title = "Additivity of trace classes"
order = 565
uses = ["sk-d-curve-pieces", "sk-d-integral", "sk-d-local-term", "sk-d-trace-class", "sk-thm-sf-kunneth-verdier"]
tags = ["sketch"]
+++
Let $c:C\to X\times X$ be a correspondence and let $\mathcal K$ be a
finitely filtered complex, an object of the filtered derived category of
$X$, with underlying complex $K$ and graded pieces $K_a$ in $D^b_{\mathrm{ctf}}(X,A)$.
Let $\tilde u:c_2^*\mathcal K\to c_1^!\mathcal K$ be a cohomological
correspondence on $\mathcal K$ in the filtered derived category, with
underlying correspondence $u$ on $K$ and induced cohomological
correspondences $u_a$ on $K_a$. Then

$$
\operatorname{Tr}_{c,K}(u)
=\sum_a\operatorname{Tr}_{c,K_a}(u_a)
\quad\text{in }H^0(\Fix(c),\omega_{\Fix(c)}).
$$

In particular, let $i:Z\hookrightarrow X$ be closed and
$j:U=X\setminus Z\hookrightarrow X$, and suppose

$$
c_1^{-1}(Z)\subset c_2^{-1}(Z),
\qquad\text{equivalently }c_2^{-1}(U)\subset c_1^{-1}(U).
$$

Write $K_U=j_!j^*K$ and $K_Z=Ri_*i^*K$ for the two pieces of the
localization triangle $K_U\to K\to K_Z$. Then $u$ has
a canonical lift, unique up to contractible choice, to a filtered
correspondence on this triangle, with induced
correspondences $u_U$ on $K_U$ and
$u_Z$ on $K_Z$, and

$$
\operatorname{Tr}_c(u)=\operatorname{Tr}_c(u_U)
+\operatorname{Tr}_c(u_Z).
$$

The induced correspondence $u_Z$ on $K_Z$ is the proper
pushforward, along $i$ and $C_Z\hookrightarrow C$, of the restriction
of $u$ to the correspondence
$C_Z=(c_1^{-1}(Z))_{\mathrm{red}}\to Z\times Z$.

*Complement (graph correspondences).* Let $s$ be the spectrum of a field, $X$
quasi-compact and compactifiable over $s$, and let $(K,\varphi)$ be a Weil
complex on $X$ in the sense of [sk-d-weil], with $K\in D^b_{ctf}(X,A)$ and
arbitrary (not necessarily invertible) Frobenius coefficient morphism
$\varphi$; fix $m\ge0$. Let $i:Z\to X$ be a closed immersion and $j:U\to X$ the
complementary open immersion, with endomorphisms $\Phi_Z$ of $Z$ and $\Phi_U$
of $U$ such that $\Phi_mi=i\Phi_Z$ and the square $\Phi_mj=j\Phi_U$ is
Cartesian. Let $K^Z=Ri_*i^*K$ and $K^U=Rj_!j^*K$, assumed in
$D^b_{ctf}(X,A)$, carry the coefficient morphisms $u^Z$, $u^U$ induced by
$\varphi_m$ as in [sk-d-curve-pieces]. Then the trace classes of the graph
correspondences $(1,\Phi_m)$ satisfy

$$
\Tr_{(1,\Phi_m)}(\varphi_m)=\Tr_{(1,\Phi_m)}(u^Z)+\Tr_{(1,\Phi_m)}(u^U)
$$

as maps $A_F\to\omega_F$ on the fixed scheme $F=\Fix(1,\Phi_m)$.
