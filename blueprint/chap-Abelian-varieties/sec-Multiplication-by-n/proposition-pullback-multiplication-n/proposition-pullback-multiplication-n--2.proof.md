+++
kind = "proof"
of = "proposition-pullback-multiplication-n--2"
order = 1500003
uses = ["theorem-theorem-cube", "lemma-abelian-variety-commutative"]
+++
Write $p_1,p_2,p_3$ for the projections from $A\times A\times A$ and
$m_{12},m_{13},m_{23},m_{123}$ for the sums of the indicated coordinates.
Since $A$ is geometrically integral by
[lemma-abelian-variety-commutative], the theorem of the cube
[theorem-theorem-cube] gives

$$
m_{123}^*\mathcal N\otimes p_1^*\mathcal N\otimes
p_2^*\mathcal N\otimes p_3^*\mathcal N
\simeq
m_{12}^*\mathcal N\otimes m_{13}^*\mathcal N\otimes
m_{23}^*\mathcal N.
$$

Indeed, on each slice through the identity, the two sides become the
same tensor product: the factor pulled back along the constant map to
the identity is trivial. This is `AlgebraicGeometry.nonempty_iso_cube`.

Compare isomorphism classes of sheaves under tensor product, writing
$u$ for the class of $\mathcal N$ and $t_m$ for that of
$[m]^*\mathcal N$. The class $u$ is a unit, since
$\mathcal N\otimes\mathcal N^{-1}\simeq\mathcal O_A$.
The constant and identity maps give $t_0=1$ and $t_1=u$.
Pulling the cube relation back along $x\mapsto(x,x,-x)$ and using
symmetry gives $t_2=u^4$. Pulling it back along
$x\mapsto(x,x,[m]x)$, for $m\geq0$, gives

$$
t_{m+2}u^2t_m=t_2t_{m+1}^2.
$$

Inductively assume $t_m=u^{m^2}$ and $t_{m+1}=u^{(m+1)^2}$.
Substitution in this relation and cancellation of the unit
$u^{m^2+2}$ give $t_{m+2}=u^{(m+2)^2}$, since
$4+2(m+1)^2=(m+2)^2+m^2+2$. Induction on the pair of consecutive
indices proves $t_n=u^{n^2}$ for every $n\geq0$. The class of
$\mathcal N^{\otimes n^2}$ is $u^{n^2}$, so this equality of
isomorphism classes yields the required isomorphism.
