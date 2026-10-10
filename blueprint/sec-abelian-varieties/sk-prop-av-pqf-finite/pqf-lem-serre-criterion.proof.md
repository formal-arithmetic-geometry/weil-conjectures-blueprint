+++
kind  = "proof"
of    = "pqf-lem-serre-criterion"
+++
*Reference: Stacks Project, Cohomology of Schemes, Lemma 30.3.2,
[Tag 01XG](https://stacks.math.columbia.edu/tag/01XG).* We outline the
argument of loc. cit.

**Step 1: affine neighbourhoods of closed points of the form $X_f$.** Let
$x\in X$ be a closed point and $U\ni x$ an affine open. Let
$\mathcal I\supseteq\mathcal I'$ be the quasi-coherent ideals of the
reduced closed subschemes $Z=X\smallsetminus U$ and $Z\cup\{x\}$. Then
$\mathcal I/\mathcal I'$ is the skyscraper sheaf $\kappa(x)$ at $x$. As $X$
is quasi-compact and quasi-separated, $\mathcal I'$ is the filtered union of
its quasi-coherent subideals of finite type, and $\mathrm H^1(X,-)$ commutes
with filtered colimits on such $X$; so $\mathrm H^1(X,\mathcal I')=0$, and
$\Gamma(X,\mathcal I)\to\kappa(x)$ is surjective. Choose
$f\in\Gamma(X,\mathcal I)\subseteq\Gamma(X,\mathcal O_X)$ with $f(x)\ne0$.
Then $X_f\subseteq U$, so $X_f=U_f$ is affine and contains $x$.

**Step 2: $X$ is affine.** Every nonempty closed subset of the quasi-compact
$X$ contains a closed point, so the open sets $X_f$ of Step 1 cover $X$, and
finitely many, $X_{f_1},\dots,X_{f_n}$, suffice. The morphism
$\mathcal O_X^{\oplus n}\to\mathcal O_X$, $(g_i)\mapsto\sum_if_ig_i$, is
surjective; its kernel $\mathcal K$ has a finite filtration
$\mathcal K\cap\mathcal O_X^{\oplus i}$ whose graded pieces are
quasi-coherent ideals of $\mathcal O_X$, so by the same colimit argument
$\mathrm H^1(X,\mathcal K)=0$. Hence $\Gamma(X,\mathcal O_X)^{\oplus n}\to
\Gamma(X,\mathcal O_X)$ is surjective, i.e. $f_1,\dots,f_n$ generate the
unit ideal of $\Gamma(X,\mathcal O_X)$. A scheme covered by affine opens
$X_{f_i}$ with $f_i\in\Gamma(X,\mathcal O_X)$ generating the unit ideal is
affine: the canonical morphism $X\to\Spec\Gamma(X,\mathcal O_X)$
restricts over each $D(f_i)$ to
$X_{f_i}\to\Spec\Gamma(X,\mathcal O_X)_{f_i}$, which is an isomorphism
because $\Gamma(X_{f_i},\mathcal O_X)=\Gamma(X,\mathcal O_X)_{f_i}$ for
quasi-compact quasi-separated $X$ and $X_{f_i}$ is affine; and the $D(f_i)$
cover the spectrum. So $X$ is affine.
