+++
kind = "proof"
of = "sk-prop-input-spreading"
+++
This is [Stacks, Tag 0EZJ](https://stacks.math.columbia.edu/tag/0EZJ); its Noetherian form is
[Stacks, Tag 0EYJ](https://stacks.math.columbia.edu/tag/0EYJ).
All three hypotheses are used: the splitting over the section, the
geometric connectedness of the fibres, and the invertibility of
$|G|$ on all of $S$; invertibility on the generic fibre is not
enough.

The proof first treats a Noetherian base, extending the cover point by
point over $S$, and then reaches a general base by a limit argument.
Over a
DVR, prime-to-residue-characteristic ramification is tame.
The section's split fibre removes the possible ramification
near the section; irreducibility of the smooth connected
special fibre and the extension lemmas for tame covers give
the finite étale extension. Over a normal Noetherian base,
extend the cover over a maximal open subset of $S$ and show that no
point is missing. At a missing point of dimension
one use the DVR case. At a missing point of dimension at
least two use depth at least two and the extension of finite
covers across the punctured base. Locally on $S=\operatorname{Spec}A$,
the completion of $C$ along the section is $A[[t_1,\ldots,t_r]]$, where
$r$ is the relative dimension; the split cover there
ensures that the resulting finite cover is étale.
This is algebraic purity for finite étale covers. The ramification,
depth and algebraic extension arguments are those of
[Stacks, Tag 0EYJ](https://stacks.math.columbia.edu/tag/0EYJ),
which uses [Stacks, Tag 0EYG](https://stacks.math.columbia.edu/tag/0EYG),
[Stacks, Tag 0EYH](https://stacks.math.columbia.edu/tag/0EYH),
[Stacks, Tag 0EYI](https://stacks.math.columbia.edu/tag/0EYI) and
[Stacks, Tag 0EYE](https://stacks.math.columbia.edu/tag/0EYE).

For a general qcqs normal integral $S$, write $S$ as an
affine-transition limit of normal integral finite-type
$\mathbf Z$-schemes. Descend the smooth family, its
section, the finite generic cover, its $G$-action, and its
rational point to a common stage. Enlarge that stage so
that the fibres are geometrically connected and $|G|$ is
invertible. Apply the Noetherian result there and pull back.
This is the limit step in [Stacks, Tag 0EZJ](https://stacks.math.columbia.edu/tag/0EZJ). It is
needed because the normal ring in [sk-lem-universal-datum]
can be non-Noetherian.

*Complement.* The generic fibre $C_\eta$ is connected,
the fibres of $C\to S$ being geometrically connected. Let $Z_0\subseteq Z$
be a connected component and $G\subseteq M$ its stabiliser. Then
$Z_0\to C_\eta$ is a connected finite étale Galois cover with group $G$, and
$Z\cong M\times^GZ_0$ is the torsor induced from it; $|G|$ divides $|M|$, so
it is invertible on $S$. The fibre $Z_{\sigma(\eta)}$ is a disjoint union of
copies of $\Spec\kappa(\eta)$, since it has a rational point and $M$ acts
simply transitively; $Z_0\to C_\eta$ is finite étale and surjective onto the
connected $C_\eta$, so $Z_0$ has a point over $\sigma(\eta)$, and that point
is $\kappa(\eta)$-rational. If $\widetilde Z_0\to C$ is a Galois cover with
group $G$ extending $Z_0$, then $\widetilde Z=M\times^G\widetilde Z_0$ is an
$M$-torsor on $C$, and the $M$-equivariant map
$Z\cong M\times^GZ_0\to M\times^G\widetilde Z_0$ makes the square with
$C_\eta\to C$ Cartesian. So it suffices to treat a connected Galois cover
$Z\to C_\eta$ with group $G$, $|G|$ invertible on $S$, with a
$\kappa(\eta)$-rational point over $\sigma(\eta)$; this is the theorem above.

