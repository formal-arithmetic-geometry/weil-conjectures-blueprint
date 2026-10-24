+++
kind  = "proof"
of    = "sk-prop-av-tate-rank"
+++
By [sk-prop-av-ntorsion-etale], the group
$A[\ell](\bar k)$ has order $\ell^{2g}$. Since it is killed by $\ell$,
it is a vector space of dimension $2g$ over $\mathbf F_\ell$. Since $A(\bar k)$
is divisible ([sk-prop-av-divisible]), we have exact sequences

$$
 0\longrightarrow A[\ell](\bar k)
 \longrightarrow A[\ell^{n+1}](\bar k)
 \xrightarrow{[\ell]}A[\ell^n](\bar k)\longrightarrow0.
$$

Choose a basis of $A[\ell](\bar k)$ and lift it successively along
$[\ell]$. Suppose that $x_1,\ldots,x_{2g}\in A[\ell^{n+1}](\bar k)$ lift
a basis of $A[\ell^n](\bar k)$ obtained in this way, so that
$\ell^nx_1,\ldots,\ell^nx_{2g}$ is the chosen basis of $A[\ell](\bar k)$.
Applying $[\ell]$ to a relation between the $x_i$, we see that all its
coefficients are divisible by $\ell^n$. The relation then becomes a
relation between the elements $\ell^nx_i$ of the chosen basis of
$A[\ell](\bar k)$, which shows that the coefficients are divisible
by $\ell^{n+1}$. Since $A[\ell^{n+1}](\bar k)$ has order
$\ell^{2g(n+1)}$, the $x_i$ form a basis of it over $\Z/\ell^{n+1}$.
Passing to the inverse limit of these compatible bases ([sk-def-av-tate]), we obtain both
isomorphisms and the description of $T_\ell A/\ell^nT_\ell A$.

The group schemes $A[\ell^n]$ and the maps $[\ell]$ are defined over
$k$, so the groups and maps in the statement commute with the action
of $\operatorname{Gal}(\bar k/k)$, although the chosen bases need not.
Finally, since $A[\ell^n]$ is finite étale ([sk-prop-av-ntorsion-etale]), it becomes a finite
disjoint union of points over $\bar k$, and its points and the
multiplication maps do not change under a further algebraically closed
extension. Tensoring with $\Q_\ell$ gives the complement.
