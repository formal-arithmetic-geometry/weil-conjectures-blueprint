+++
id = "prose-P1-01"
kind = "hidden"
title = "The six operations"
order = 22
+++
On the étale site the constant sheaf $\mathbf Z_\ell$ on
$\operatorname{Spec}\mathbf F_q$ has $H^1=0$, although
$\varprojlim_nH^1(\operatorname{Spec}\mathbf F_q,\mathbf Z/\ell^n)=\mathbf Z_\ell$
(Section [sec-Weil-cohomology]). Moreover, Frobenius eigenvalues live in
$\overline{\mathbf Q}_\ell$, but SGA 4 constructs $Rf_!$ and $f^!$ and proves the finiteness
theorems only for $\mathbf Z/\ell^n$ [sga4], [sga4-5]. So the theory we need is not the one SGA 4 provides. This part has to
overcome two difficulties. The first concerns the coefficients: we must pass
to the limit over $n$ without losing cohomology.
Classically one does this with systems $(F_n)$ and makes every derived
construction by hand [ekedahl90]. We work instead on the pro-étale site
of Bhatt and Scholze (Chapter [chap-The-pro-etale-site]). There $\mathbf Z_\ell$ is a sheaf
of rings with the expected cohomology, and one definition serves all the
coefficient rings

$$
A,\ \mathbf Z_\ell,\ \mathcal O_E,\ \mathbf Q_\ell,\ E,\ \overline{\mathbf Q}_\ell,
$$

compatibly with every change of coefficients between them
(Section [sec-Change-of-coefficients]).

What the rest of the notes needs from this part is the table of
Section [sec-The-function-sheaf-dictionary]: for every morphism $f$ of schemes of finite
type over $k$, the operations $f^*$, $Rf_*$, $Rf_!$, $f^!$,
$\otimes^{\mathbf L}$ and $\cHom$, with their adjunctions, base change and
projection formulas, and the finiteness statement that each carries
constructible complexes to constructible complexes
(Theorem [theorem-exceptional-inverse-image] and
Proposition [proposition-six-operations-dctf]). The later parts use these
operations as their basic tools. For example, the trace formula of
Part II sums trace functions over the fibres of $f$ by
applying $Rf_!$, and Poincaré duality comes from the computation of
$f^!\Lambda$ for the structure morphism $f$ of a smooth variety. Similarly,
the Fourier transform of Part III is built from $f^*$,
$\otimes^{\mathbf L}$ and $Rf_!$.

The second difficulty is to show that $f^!$ preserves constructible
complexes, and it would be there even with finite coefficients. It arises
because $f^!$ is given only by its universal property, and already for a
closed immersion $i$ with open complement $j$ its value is not obvious: we know only that $i^!K$
sits in a triangle $i^!K\to i^*K\to i^*Rj_*j^*K$. To see that it is
constructible we need to know that $Rj_*$ preserves constructibility, and this
is Deligne's generic base change theorem. Accordingly, we construct $f^!$ in
Chapter [chap-Construction-of-f] and prove that it preserves
constructible complexes in Chapter [chap-Constructibility-of-f], as
sketched in Section [sec-The-six-operations].

The two difficulties are handled separately, so that each geometric
argument is made only once. The geometric inputs, namely proper base change
(Chapter [chap-Proper-base-change]) and the computation of $f^!$ on
charts (Chapter [chap-Constructibility-of-f]), are proved with
torsion coefficients on the étale site, where SGA 4 applies. They are then
transferred to $\ell$-adic coefficients without being proved again. Two
facts make this transfer possible
(Chapters [chap-Constructible-complexes]
and [chap-The-six-operations-on-Dbctf]). First, a constructible complex over
$\mathcal O_E$ is determined by its reductions modulo $\pi_E^n$
(Proposition [proposition-integral-constructibility-criterion]), so its
properties can be read off from torsion complexes. Second, whether a natural
map between two such constructions is an isomorphism can be checked with
finite coefficients
(Proposition [proposition-isomorphisms-reduce-finite-coefficients]). For
example, smooth base change for $\mathbf Z_\ell$, $E$ and $\overline{\mathbf Q}_\ell$ follows from smooth
base change for finite rings in this way (Section [sec-ell-adic-coefficients-3]).
