+++
kind = "proof"
of = "sk-prop-sf-open-closed-triangle"

+++
The main assertion is the one about limits, and it is local on $X$. Let $V$
be a weakly contractible object of the affine ind-étale basis of $Z$. It has
a canonical henselian lift $v(V)$ in the corresponding basis of $X$: the
functor $v$ is the fully faithful left adjoint to base change of these affine
bases, and $v(V)\times_XZ\simeq V$ (Stacks, Tag 09A9). The pullback of a
sheaf, evaluated on $V$, is its evaluation on $v(V)$, because every covering
of a weakly contractible object splits and therefore sheafification does not
change values there. Since evaluation commutes with limits and these objects
detect isomorphisms, it follows that $i^*$ preserves limits. As a left
adjoint it preserves colimits, and it is exact. Lifting covers through the
henselian thickenings, we obtain exactness of $i_*$ and the identities
$i^*i_*=\mathrm{id}$ and $j^*i_*=0$. The open–closed sequence follows by the
same descent along covers, or from its description by kernels.

On derived categories we obtain, for $K\in D(U_{\mathrm{proét}},j^*B)$, the
triangle

$$
j_!K\longrightarrow Rj_*K\longrightarrow i_*i^*Rj_*K\longrightarrow j_!K[1]
\quad\text{in }D(X_{\mathrm{proét}},B).
$$

Its last two terms preserve products and derived inverse limits, and hence so
does their fibre $j_!$. Since $j_!$ is exact and products are exact, we get
the corresponding statements about limits of sheaves of modules. The argument
with henselian thickenings is Bhatt–Scholze, §6.1; see also Stacks, Tags
09AA, 09AH, 09BM and 09BP.
