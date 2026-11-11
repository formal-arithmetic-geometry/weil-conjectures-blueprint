+++
kind = "proof"
of = "lemma-simple-objects"
order = 1259
uses = ["proposition-etale-implications", "definition-w-local-w-strictly-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "lemma-comparison-completed-coefficients", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "proposition-integral-constructibility-criterion", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-base-change-complete-integral", "proposition-comparison-etale-derived-category", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "proposition-sp-unique-adjoint", "lemma-boundary-stalk", "lemma-largest-punctual-subsheaf", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
Since a middle extension has no punctual subobject or
quotient and $M$ is irreducible on the open, the
middle extension is simple. Conversely, ordinary truncation splits an arbitrary perverse
sheaf into a punctual part and a part of the form $F[1]$, and
simplicity forces one of them to vanish.

We first show that $P=(j_*M)[1]$ has no punctual subobject or quotient.
The adjunction calculations below are geometric, so they apply equally
to compatible Weil morphisms. Let $i$ be the inclusion of a finite set
of closed points and $A$ a sheaf on it. A map $P\to i_*A$ is zero, because by
adjunction it corresponds to a map from $i^*P=(i^*j_*M)[1]$ to the
sheaf $A$, that is, to a negative Ext. A map in the other direction is
also zero, and to see this we first enlarge the boundary. Since $M$ is lisse, $j_*M$ does not change when we replace $U$
by a smaller dense open and $M$ by its restriction, so we may assume that the support of $A$ lies in
$Z=C\setminus U$, and we let $i$ now denote the inclusion of $Z$. Then the
adjunction $j^*\dashv Rj_*$ shows that $i^!Rj_*M=0$. In the triangle

$$
j_*M\longrightarrow Rj_*M\longrightarrow
\tau^{\ge1}Rj_*M\longrightarrow
$$

the last term is supported on $Z$, so that $i^!$ agrees with $i^*$ on
it. Applying $i^!$ and using $i^!Rj_*M=0$, we find
$i^!j_*M\simeq(i^*\tau^{\ge1}Rj_*M)[-1]$, which has ordinary
cohomology only in degrees at least two. Hence $i^!P$ has ordinary
cohomology only in degrees at least one.
Therefore $\Hom(i_*A,P)=\Hom(A,i^!P)=0$.

To see that $P$ is simple, note that on a dense open a
perverse subobject of $P$ is a shifted lisse subsheaf of $M$. By
irreducibility it is $0$ or everything there, and the difference is
then punctual. In detail, consider a perverse exact sequence
$0\to Q\to P\to R\to0$, restrict it to a smaller dense open on which
all ordinary cohomology sheaves are lisse. There $P=M[1]$, and the
sequence is a shifted exact sequence of lisse sheaves. Moreover, restriction to
a dense open preserves irreducibility, because the fundamental group
of a dense open of a normal connected curve surjects onto that of the
curve, as in the proof of Theorem [theorem-purity-real-sheaves-curves], and the same
holds for the Weil groups. Hence $Q$ or $R$ has zero generic
restriction. Such a perverse object is
punctual. Indeed, its $\mathcal H^{-1}$ is then supported on a finite
set, and a sheaf without punctual subsheaves with this property is
zero, while its $\mathcal H^0$ is punctual by definition. Thus $Q$ or $R$
is a punctual subobject or quotient of $P$, which by the vanishing just
proved is zero, and so $P$ is simple.

Conversely, let $P$ be simple. We show that $P$ is punctual or a middle
extension of an irreducible lisse sheaf. Ordinary truncation gives a
perverse exact sequence

$$
0\longrightarrow(\mathcal H^{-1}P)[1]
\longrightarrow P\longrightarrow\mathcal H^0P\longrightarrow0.
$$

Hence a simple $P$ is either punctual or of the form $F[1]$, where $F$
has no punctual subsheaf. In the second case, choose a dense open $U$
on which $F$ is lisse and put $M=F|_U$.
Then the map $F\to j_*M$ is injective, since its kernel is $F_{\rm p}=0$
(Lemma [lemma-largest-punctual-subsheaf]),
and its cokernel $B$ is punctual. Rotating the corresponding triangle of sheaves we obtain the perverse
exact sequence $0\to B\to F[1]\to(j_*M)[1]\to0$, whose last term is
nonzero, so $B=0$ by simplicity. It remains to see that $M$ is
irreducible. Suppose that $M$ had a proper nonzero
lisse subsheaf $M_1$. Then the object $j_!M_1[1]$ is perverse, because
$j_!M_1\subset j_*M_1$ has no punctual subsheaf, and the image of
$j_!M_1[1]\to P$ in the abelian heart is proper and nonzero, as one
sees on $U$. This contradicts simplicity. Finally, if $P$ is punctual, then by the
long exact cohomology sequence its subobjects in the heart are
punctual sheaves in degree zero, so $P$ is simple exactly when it is
irreducible as a punctual sheaf.
