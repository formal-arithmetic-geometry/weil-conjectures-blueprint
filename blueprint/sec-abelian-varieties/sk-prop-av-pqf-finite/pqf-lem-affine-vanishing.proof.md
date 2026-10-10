+++
kind  = "proof"
of    = "pqf-lem-affine-vanishing"
+++
*Reference: Stacks Project, Cohomology of Schemes, Lemma 30.2.2,
[Tag 01XB](https://stacks.math.columbia.edu/tag/01XB).* We outline the
argument of loc. cit. Replacing $X$ by $U$ we may assume $X=\Spec A$ affine
and $\mathcal F=\widetilde M$. For a standard open covering
$X=\bigcup_{i=1}^nD(f_i)$ with $(f_1,\dots,f_n)=A$, the Čech complex of
$\widetilde M$ is the complex
$M\to\prod_iM_{f_i}\to\prod_{i<j}M_{f_if_j}\to\cdots$; it is exact,
because exactness may be checked after localising at each $f_j$, and after
inverting $f_j$ the covering contains the whole space, so the localised
complex is contractible. Standard opens form a basis of $X$ stable under
finite intersections, each of them again affine, so the Čech cohomology of
$\mathcal F$ vanishes in positive degrees for every standard open covering of
every standard open. By Cartan's criterion (a sheaf whose higher Čech
cohomology vanishes for all coverings in such a basis has vanishing higher
derived-functor cohomology on the members of the basis; Stacks Project,
Cohomology of Sheaves, Section 20.11), we get
$\mathrm H^p(X,\mathcal F)=0$ for $p>0$.
