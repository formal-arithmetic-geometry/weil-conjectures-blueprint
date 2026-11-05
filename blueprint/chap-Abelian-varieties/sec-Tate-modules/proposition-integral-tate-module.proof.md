+++
kind = "proof"
of = "proposition-integral-tate-module"
order = 1513
uses = ["lemma-acyclic-resolutions", "lemma-schematic-closure-uniqueness", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n"]
+++
A finite abelian group of order $\ell^{2gn}$ killed by $\ell^n$ need not
be free over $\mathbf Z/\ell^n$; for $g\geq1$ the group
$(\mathbf Z/\ell^2)^{2g-2}\oplus(\mathbf Z/\ell)^{4}$ has order $\ell^{4g}$
and is killed by $\ell^2$. For $A[\ell^n]$, however, this cannot happen because
we know the orders at every level together with the exact
sequences given by $[\ell]$. Indeed, we use them to lift a basis of the
$\ell$-torsion step by step and check by counting that the lifts form
a basis at each level.

*The $\ell$-torsion and the exact sequences.* The group
$A[\ell](\bar k)$ is a vector space of dimension $2g$ over $\Fell$, since
it is killed by $\ell$ and has order $\ell^{2g}$ by
Proposition [proposition-multiplication-n]. Moreover there are exact
sequences

$$
0\longrightarrow A[\ell](\bar k)
\longrightarrow A[\ell^{n+1}](\bar k)
\xrightarrow{[\ell]}A[\ell^n](\bar k)\longrightarrow0,
$$

whose surjectivity holds because $A(\bar k)$ is divisible: every point of
$A[\ell^n](\bar k)$ is $\ell$ times a point, which then lies in
$A[\ell^{n+1}](\bar k)$.

*Lifting bases.* Choose a basis of $A[\ell](\bar k)$ and lift it
successively along $[\ell]$; the lifts form a basis at each level.
Suppose that $x_1,\ldots,x_{2g}\in A[\ell^{n+1}](\bar k)$ lift
a basis of $A[\ell^n](\bar k)$ obtained in this way, so that
$\ell^nx_1,\ldots,\ell^nx_{2g}$ is the chosen basis of $A[\ell](\bar k)$.
To see that the $x_i$ are independent, note first that all coefficients of a relation between them are divisible by
$\ell^n$, as we see by applying $[\ell]$ to it. The relation then becomes a
relation between the elements $\ell^nx_i$ of the chosen basis of
$A[\ell](\bar k)$, so the coefficients are even divisible by $\ell^{n+1}$.
As $A[\ell^{n+1}](\bar k)$ has order $\ell^{2g(n+1)}$, the $x_i$ therefore
form a basis of it over $\mathbf Z/\ell^{n+1}$.
Passing to the inverse limit of these compatible bases, we obtain both
isomorphisms and the description of $T_\ell A/\ell^nT_\ell A$.

*Equivariance and independence of $\bar k$.* The groups and maps in
the statement commute with the action of $\operatorname{Gal}(\bar k/k)$,
because the group schemes $A[\ell^n]$ and the maps $[\ell]$ are defined
over $k$. In particular the projection
$T_\ell A/\ell^nT_\ell A\to A[\ell^n](\bar k)$ is equivariant. The
chosen bases need not be equivariant, which is why the isomorphisms
with $(\mathbf Z/\ell^n)^{2g}$ and $\mathbf Z_\ell^{2g}$ are noncanonical.
Finally, the points of $A[\ell^n]$ and the multiplication maps do not
change under a further algebraically closed extension, because
$A[\ell^n]$ is finite étale and hence a finite disjoint union of points
over $\bar k$.
