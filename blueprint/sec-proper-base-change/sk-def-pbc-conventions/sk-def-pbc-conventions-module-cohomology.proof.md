+++
kind = "proof"
of = "det-pbc-conventions-module-cohomology"
+++
*(1)* Let $\mathfrak U=\{U_i\to U\}_{i\in A}$ be an étale covering of an étale
$T$-scheme $U$, and for a finite tuple $i_0,\dots,i_p$ write
$j_{i_0\cdots i_p}:U_{i_0\cdots i_p}=U_{i_0}\times_U\cdots\times_UU_{i_p}\to T$.
Let $\Lambda_{V}=j_!\Lambda$ denote the extension by zero of the constant
module sheaf along an étale $j:V\to T$; it represents
$G\mapsto G(V)$ on $\Mod(T_{\Et},\Lambda)$. The complex of module sheaves

$$
\cdots\to\bigoplus_{i_0,i_1}\Lambda_{U_{i_0i_1}}\to
\bigoplus_{i_0}\Lambda_{U_{i_0}}\to\Lambda_U\to0
$$

(alternating sums of the projections as differentials) is exact: on the
stalk at a geometric point $\bar t$ it is the augmented chain complex of
$\Lambda$-linear combinations on the simplicial set
$E_p=\{(i_0,\dots,i_p,\text{lift of }\bar t)\}$ over each lift of $\bar t$
to $U$, and since $\mathfrak U$ is a covering each lift of $\bar t$ to $U$
lifts to some $U_i$, so this simplicial set is a cone (insert a fixed index in
front) and its augmented chain complex is contractible. Applying the exact
functor $\Hom_\Lambda(-,I)$ gives the Čech complex
$\check C^\bullet(\mathfrak U,I)$, augmented by $I(U)$, which is therefore
exact. So $\check H^p(\mathfrak U,\mathrm{For}\,I)=0$ for $p>0$ for all
coverings of all étale $U$. By Cartan's criterion (Stacks Project, Cohomology on Sites, section on Čech
cohomology and cohomology; this is the argument of Tag 03FD),
an abelian sheaf whose higher Čech cohomology vanishes for every covering of
every object has vanishing higher cohomology on every object. This proves (1).

*(2)* Choose an injective resolution $F\to I^\bullet$ in
$\Mod(T_{\Et},\Lambda)$. Since $\mathrm{For}$ is exact,
$\mathrm{For}\,F\to\mathrm{For}\,I^\bullet$ is a resolution, by (1) consisting
of $\Gamma(U,-)$-acyclic abelian sheaves. By the acyclic-resolution lemma
[lemma-weil-pbc-leray-acyclicity],
$H^q(\Gamma(U,\mathrm{For}\,I^\bullet))\cong H^q(U,\mathrm{For}\,F)$, while
the left side is by definition $\mathrm{For}\,H^q_\Lambda(U,F)$. Independence
of the resolution follows from uniqueness of comparison maps up to homotopy.

*(3)* For an abelian sheaf $G$ on $S_{\Et}$, $R^qu_*G$ is the sheafification
of $V\mapsto H^q(S\times_TV,G)$ on étale $V\to T$, and the same holds for
module sheaves with module cohomology. For an injective module sheaf $I$ on
$S_{\Et}$, (1) applied on $S$ to the étale objects $S\times_TV$ gives
$R^qu_*\mathrm{For}\,I=0$ for $q>0$. Thus for a module-injective resolution
$F\to I^\bullet$, the resolution $\mathrm{For}\,F\to\mathrm{For}\,I^\bullet$ is
$u_*$-acyclic, and [lemma-weil-pbc-leray-acyclicity] gives
$R^qu_*\mathrm{For}\,F\cong H^q(u_*\mathrm{For}\,I^\bullet)=
\mathrm{For}\,H^q(u_*I^\bullet)=\mathrm{For}\,R^qu_*F$, using
$\mathrm{For}\circ u_*=u_*\circ\mathrm{For}$. For $K\in D^+(S_{\Et},\Lambda)$
choose a bounded below complex of injective module sheaves $I^\bullet$
quasi-isomorphic to $K$; then $\mathrm{For}\,I^\bullet$ is a bounded below
complex of $u_*$-acyclic sheaves quasi-isomorphic to $\mathrm{For}\,K$, and
the complex form of [lemma-weil-pbc-leray-acyclicity] identifies
$Ru_*\mathrm{For}\,K$ with $u_*\mathrm{For}\,I^\bullet=\mathrm{For}\,u_*I^\bullet
=\mathrm{For}\,Ru_*K$.
