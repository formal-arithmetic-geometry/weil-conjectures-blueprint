+++
kind  = "proof"
of    = "thm-trf-fixed-point-localization"
+++
All morphisms below are separated and of finite type between separated
finite-type $k$-schemes, hence exceptionally admissible at the finite
stage ([thm-sf-preservation-class]).

*The pushforward to the point.* Since $a_C=a_Xc_2$ with $a_X$ and $c_2$
proper, $C$ is proper over $s$, and $a_C=a_Xc_1$ as well. Let
$b=(\operatorname{id}_s,\operatorname{id}_s):s\to s\times_ss$ be the
point correspondence. Then $(f,g)=(a_X,a_C):(C,c)\to(s,b)$ is a proper
pushforward diagram of [def-trf-coefficient-pushforward]
($b_ig=a_C=a_Xc_i$). Its fixed scheme is $\operatorname{Fix}(b)=s$, and
the induced map of fixed schemes is the structure morphism
$h=a_F:F\to s$. Put $K'=Ra_{X*}K$; since $a_X$ is proper,
$Ra_{X*}=Ra_{X!}$ ([prop-functor-package], clause (3)), so
$K'=R\Gamma_c(X,K)$, a perfect $A$-complex by
[prop-trf-compact-support-perfectness].

*The pushed coefficient map is the global operator.* In
[def-trf-coefficient-pushforward], the ordinary half $\gamma$ is the unit
$\eta_{a_C}$ followed by $Ra_{C*}c_2^*\varepsilon_{a_X}$. Because
$a_C=a_Xc_2$, the unit $\eta_{a_C}$ is $\eta_{a_X}$ followed by
$Ra_{X*}\eta_{c_2}a_X^*$, and the triangle identity
$(Ra_{X*}\varepsilon_{a_X})\circ(\eta_{a_X}Ra_{X*})=\operatorname{id}$ of
[fix-prop-adjunctions] cancels the counit; hence
$\gamma=Ra_{X*}\eta_{c_2}$, followed by $Ra_{X*}Rc_{2*}=Ra_{C*}$ and
$Rc_{2*}=Rc_{2!}$. These are the first two arrows of
[def-trf-global-operator]. For $b_1=\operatorname{id}_s$ the exceptional
adjoint in the exceptional half is the identity, so $\delta$ is the
composition isomorphism $\Xi_1$ of [thm-sf-comp-composition] followed by
$Ra_{X!}\varepsilon_{c_1}$, which are the last two arrows of
[def-trf-global-operator]. Therefore

$$
[a_X,a_C]_!u=T_c(u):R\Gamma_c(X,K)\longrightarrow R\Gamma_c(X,K)
$$

as an endocorrespondence of $K'$ with support $s$.

*Proper pushforward compatibility.* By
[thm-trf-trace-proper-compatibility],

$$
(a_F)_*\operatorname{Tr}_c(u)=\operatorname{Tr}_b\bigl(T_c(u)\bigr)
\qquad\text{in }\operatorname{Hom}(A_s,\omega_s)=A .
$$

Since $F$ is proper over $s$, the left side is the integral
$\int_F\operatorname{Tr}_c(u)$ by [lem-trf-integration-as-pushforward].

*Point normalization.* The correspondence $b$ is the diagonal of $s$, so
by [lem-trf-trace-class-diagonal-pairing] the trace class
$\operatorname{Tr}_b(T_c(u))$ is the supported pairing
$\langle T_c(u),1_{K'}\rangle_{\mathrm{LV}}$, and by
[prop-trf-pairing-point-normalization], applied to the perfect complex
$P=K'$ with $u=T_c(u)$ and $v=1_{K'}$, this pairing is
$\operatorname{tr}_A(T_c(u)\mid R\Gamma_c(X,K))$. Combining the three
displays gives

$$
\operatorname{tr}_A\bigl(T_c(u)\mid R\Gamma_c(X,K)\bigr)
=\int_F\operatorname{Tr}_c(u).
$$
