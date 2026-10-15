+++
kind = "proof"
of = "sk-thm-sf-comp-composition"
uses = ["sk-prop-proper-base-change-unbounded", "sk-prop-proper-image-localizing", "sk-lem-sf-determination", "sk-prop-sf-comp-coherence"]
+++
*The composition isomorphism.* Choose compactifications $f=p\circ j$ and
$g=q\circ i$, with $j:X\to\overline X$ and $i:Y\to\overline Y$ open and $p,q$
proper. In the composite $Rq_*i_!Rp_*j_!$ the middle factor $i_!Rp_*$ applies a
proper direct image before an extension by zero; we interchange the two.
Compactify the morphism $i\circ p:\overline X\to\overline Y$ as
$\overline X\xrightarrow{j'}W\xrightarrow{r}\overline Y$, with $j'$ open, $r$
proper and $\overline X$ dense in $W$. Then $r^{-1}(Y)=\overline X$: the open
immersion $\overline X\to r^{-1}(Y)$ is a morphism from a proper $Y$-scheme to a
separated $Y$-scheme, hence proper, so its image is closed; being also open and
dense, it is everything.

For $A$ in $D(\overline X_{\mathrm{proét}},\Lambda)$, restriction to the open
$Y\subset\overline Y$ identifies $i^*Rr_*j'_!A$ with $Rp_*A$ in
$D(Y_{\mathrm{proét}},\Lambda)$, because $r^{-1}(Y)=\overline X$. By the adjunction
$i_!\dashv i^*$ this gives a map

$$
i_!Rp_*A\longrightarrow Rr_*j'_!A\quad\text{in }D(\overline Y_{\mathrm{proét}},\Lambda),
$$

which is the unique map restricting to the identity of $Rp_*A$ over $Y$. For
$A\in\Dctf(\overline X,\Lambda)$ it is an isomorphism: over $Y$ it is the
identity, and over $\overline Y\setminus Y$ both sides vanish, the right side by
proper base change on $\Dctf$ ([sk-prop-proper-base-change-unbounded], for the
inclusion of $\overline Y\setminus Y$ into $\overline Y$) since $j'_!A$ vanishes on
$r^{-1}(\overline Y\setminus Y)=W\setminus\overline X$. Both sides preserve direct
sums on $\Loc(\Dctf(\overline X,\Lambda))$ ([sk-prop-proper-image-localizing]), so
[sk-lem-sf-determination] shows that the interchange map is an isomorphism for
all $A\in\Loc(\Dctf(\overline X,\Lambda))$. Taking $A=j_!K$ gives, in
$D(Z_{\mathrm{proét}},\Lambda)$,

$$
Rq_*i_!Rp_*j_!K\simeq Rq_*Rr_*j'_!j_!K=R(qr)_*(j'j)_!K,
$$

and the right side is $R(gf)_!K$ computed with the compactification
$gf=(qr)\circ(j'j)$.

*Canonicity and associativity.* Every map used is characterized by its
restriction to an open subscheme: the refinement maps of
[sk-prop-sf-comp-coherence] and the interchange maps above restrict to
identities. Replacing any of the chosen compactifications by a refinement
therefore commutes with the interchange map, because both composites restrict
to the same identity and are then equal by adjunction. For three composable
morphisms, choose common refinements (by graph closure) of the finitely many
compactifications that occur in the binary composites. On these, each of the
two bracketings is built from composites of proper direct images, composites
of extensions by zero, and interchange maps. Composition of proper direct
images is associative, being composition of right adjoints of the exact
inverse images, and composition of extensions by zero is associative by
adjunction. Interchanging two adjacent open and proper steps in either order
gives the same map by the uniqueness of the interchange map. Hence the two
bracketings agree; the same argument with four morphisms gives the pentagon,
and the identity constraints are the case where one compactification is the
identity. Transitivity of the refinement maps transports these equalities
back to the originally chosen compactifications.

*Base change.* Pull back a compactification $f=p\circ j$ along $v$ to a
compactification $f'=p'\circ j'$, since open immersions and proper morphisms
are stable under base change. Extension by zero commutes with inverse image:
let $v':\overline X'\to\overline X$ be the projection; the functors $v'^*j_!$ and
$j'_!u^*$ from $D(X_{\mathrm{proét}},\Lambda)$ to $D(\overline X'_{\mathrm{proét}},\Lambda)$
agree on the pulled-back open and are zero on its closed complement, which
characterizes them (Stacks, Tag 09AH). Proper base change on
$\Loc(\Dctf(\overline X,\Lambda))$ is [sk-prop-proper-base-change-unbounded].
Composing the two gives the isomorphism
$v^*Rp_*j_!\simeq Rp'_*v'^*j_!\simeq Rp'_*j'_!u^*$ of functors
$\Loc(\Dctf(X,\Lambda))\to\Loc(\Dctf(Y',\Lambda))$. It is compatible with change
of compactification because the refinement maps are characterized by their
restriction to the open subscheme.
