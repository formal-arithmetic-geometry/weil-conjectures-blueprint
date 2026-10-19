+++
kind = "proof"
of = "sk-prop-tf-nearby-external-kunneth"
uses = ["sk-lem-sf-kunneth-star"]
+++
We follow the dimension argument of (Illusie, *Autour du théorème de monodromie locale*,
Theorem 4.7, pp. 51–53), on the classical étale site. Let $p$ be the characteristic exponent of
$k$. Ordinary external Künneth over the geometric fibres is [sk-lem-sf-kunneth-star]; it applies
over the separably closed field $k$ because passing to an algebraic closure is a purely inseparable
extension and does not change the étale topos.

*Facts about traits.* Two further facts are used, both from (SGA 4½, *Théorèmes de finitude*,
§§3.4 and 3.7). First, geometric nearby cycles are invariant under extension of traits, with the
corresponding restriction of inertia action. Second, they have a generic-slicing description. Let
$s'$ be a geometric generic point of the special fibre $\mathbf A^1_k$ of $\mathbf A^1_S$, and let
$S'=(\mathbf A^1_S)_{(s')}$ be the strict localization of $\mathbf A^1_S$ at $s'$. This is a
strictly henselian trait with the same uniformizer as $S$. With compatible geometric generic
points, its inertia group fits into

$$
1\longrightarrow P\longrightarrow I'\longrightarrow I\longrightarrow1,
$$

where $P$ is pro-$p$ (and is trivial when $p=1$). For $a:W\to\mathbf A^1_S$, put
$W'=W\times_{\mathbf A^1_S}S'$ and let $N'$ be the pullback of $N\in D^b_{\mathrm{ctf}}(W_\eta,A)$.
There is a canonical identification

$$
(R\Psi_{W/S}N)|_{W_s\times_{\mathbf A^1_k}s'}\simeq(R\Psi_{W'/S'}N')^P.
\tag{2}
$$

Here $(-)^P=R\Gamma(P,-)$ is exact on the discrete prime-to-$p$ torsion coefficients under
consideration. The formula comes from factoring the geometric generic-fibre map through the
geometric generic point of $S'$, which lies over $\bar\eta$; the Galois group of the second step is
$P$. The kernel is pro-$p$ because the common uniformizer identifies the tame inertia quotients.
The formula is compatible with the pullback exchanges and product maps obtained from
$\bar i^*R\bar j_*$: factor the generic-fibre maps first and use the composition law for their
direct-image adjunctions.

The invariant functor commutes with tensoring by an object on which $P$ acts trivially: for a
complex $E$ with continuous $P$-action and a complex $B$ with trivial $P$-action, the projection map
is an isomorphism

$$
(E\mathbin{\otimes_A^{\mathbf L}}B)^P\simeq E^P\mathbin{\otimes_A^{\mathbf L}}B.
\tag{3}
$$

The reason is that $P$-invariants are exact on discrete torsion $A$-modules. On a finite quotient
$G$ of $P$, invariants are the image of the averaging idempotent $|G|^{-1}\sum_{g\in G}g$, since
the $p$-power $|G|$ is invertible in $A$; this idempotent commutes with tensoring by $B$.
Continuity passes from the finite quotients to $P$, and resolving $B$ by flat $A$-modules gives the
derived identity.

*Outline.* The cone $C$ of $\Pi_{L,M}$ has zero global sections when $X$ and $Y$ are projective, by
the ordinary Künneth formula on the two fibres; generic slicing and induction on dimension show
that $C$ has finite support, and a complex with finite support and zero global sections vanishes.
The global-sections statement rests on the compatibility of $\Pi$ with proper direct images in the
two factors.

*Proper direct images.* For proper $f:X\to X_1$ and $g:Y\to Y_1$, identify product direct images
using ordinary Künneth and identify nearby direct images using proper exchange. Then
$R(f_s\times g_s)_*\Pi_{L,M}$ becomes

$$
\Pi_{Rf_{\eta*}L,Rg_{\eta*}M}.
$$

To verify this equality, expand the two product maps as the tensor maps of $R\bar j_*$, commute
proper direct image past those generic open maps, and take the adjoints of the ordinary Künneth
arrows. Both adjoints are $f_\eta^*Rf_{\eta*}L\boxtimes g_\eta^*Rg_{\eta*}M\to L\boxtimes M$, the
tensor of the two counits. The identities of the adjunctions and their composition law therefore
identify the maps themselves.

*Reduction to projective flat families.* Induct simultaneously for all such traits on
$n=\dim(X_{\bar\eta}\times_{\bar\eta}Y_{\bar\eta})$. The assertion is local on $X_s\times_kY_s$. On
affine neighbourhoods of the two factors, take projective closures over $S$ and extend the
coefficients by zero on their generic fibres. Nearby-cycle open pullback identifies the restriction
with the original map. Thus we may assume $X,Y$ projective. Using proper exchange for the closed
immersions of the closures of their generic fibres, and nilpotent invariance, we may also assume
they are reduced and their generic fibres are dense. They are then flat over the trait. These
reductions do not increase $n$.

*Global sections.* Proper exchange for the structure maps, the compatibility with proper direct
images, and ordinary Künneth on the geometric generic fibres give, for the cone $C$ of (1),

$$
R\Gamma(X_s\times_kY_s,C)=0.
\tag{4}
$$

Under these identifications the map of global complexes is the Künneth isomorphism

$$
R\Gamma(X_{\bar\eta},L)\otimes_A^{\mathbf L}R\Gamma(Y_{\bar\eta},M)
\xrightarrow{\sim}
R\Gamma(X_{\bar\eta}\times Y_{\bar\eta},L\boxtimes M).
$$

*Finite support.* It remains to show that $C$ has finite support. When $n=0$, flatness gives
zero-dimensional special fibres and this is automatic.

For $n>0$, work on small neighbourhoods with quasi-finite coordinate maps

$$
b:X\longrightarrow\mathbf A^q_S,\qquad c:Y\longrightarrow\mathbf A^r_S,\qquad q+r\leq n.
$$

Such local relative coordinate maps exist for flat finite-type schemes over a trait. Flatness
bounds the dimensions of the special fibres by the corresponding generic dimensions. Choose local
parameter functions on the special fibres, lift them to the total spaces, and shrink to the
quasi-finite loci of the resulting maps. If the sum is smaller than $n$, induction already applies,
so consider $q+r=n$. Suppose first $q>0$ and compose $b$ with any one coordinate projection
$\mathbf A^q_S\to\mathbf A^1_S$. Use its generic slice $S'$ as above, and put

$$
X'=X\times_{\mathbf A^1_S}S',\qquad Y'=Y\times_SS',\qquad
L'=L|_{X'_{\eta'}},\quad M'=M|_{Y'_{\eta'}}.
$$

The generic dimensions satisfy

$$
\dim X'_{\bar\eta'}\leq q-1,\qquad \dim Y'_{\bar\eta'}\leq r.
$$

The product $X'_{\bar\eta'}\times Y'_{\bar\eta'}$ therefore has dimension at most $n-1$, and
induction makes $\Pi_{L',M'}$ an isomorphism. The slicing calculation, ordinary trait-change
invariance in the second factor, and the same slicing calculation on $X\times_SY$ identify the
restrictions to this slice as

$$
\begin{aligned}
R\Psi_{X/S}L|_{s'}&\simeq(R\Psi_{X'/S'}L')^P,\\
R\Psi_{Y/S}M|_{s'}&\simeq R\Psi_{Y'/S'}M',\\
R\Psi_{(X\times Y)/S}(L\boxtimes M)|_{s'}&\simeq(R\Psi_{(X'\times Y')/S'}(L'\boxtimes M'))^P.
\end{aligned}
$$

In the middle line $P$ acts trivially: the nearby-cycle complex comes by restriction from $I$, and
$P$ is the kernel of $I'\to I$. Apply $(-)^P$ to $\Pi_{L',M'}$ and use (3). The result is the
restriction of (1), by the composition compatibility in (2). It is therefore an isomorphism.

Thus $C$ restricts to zero over $s'$, so its support has no point over the generic point of this
special-fibre coordinate line. Its image in that line is constructible and omits the generic point,
so is a finite set of closed points. Repeat this argument for each of the $q$ coordinates of $b$
and, interchanging the factors, for each of the $r$ coordinates of $c$. The support is contained in
the inverse image under $b_s\times c_s$ of a finite product of finite sets. This inverse image is
finite because $b_s\times c_s$ is quasi-finite. A finite cover of $X_s\times Y_s$ by these
neighbourhoods proves that the support of $C$ is finite globally.

A bounded constructible complex supported on a finite set of closed points over a separably closed
field is the direct image of its stalk complexes on that finite closed reduced subscheme. Its
global sections are their finite direct sum and hence detect vanishing. Equation (4) therefore
gives $C=0$, completing the induction.
