+++
kind = "proof"
of = "proposition-ordinary-external-kunneth--1"
order = 719002
uses = ["proposition-proper-direct-image-constructible-complexes"]
+++
Factor $q=f_1\times f_2$ as

$$
X_1\times X_2\xrightarrow{r=f_1\times\operatorname{id}_{X_2}}
Y_1\times X_2\xrightarrow{s=\operatorname{id}_{Y_1}\times f_2}
Y_1\times Y_2.
$$

The morphisms $r$ and $s$ are base changes of $f_1$ and $f_2$, respectively,
so they are proper. In each of these cartesian squares, transport the
counit of $f_i^*\dashv Rf_{i*}$ along the projections. Its adjoint
transpose is the base change map, hence an isomorphism by
[proposition-proper-direct-image-constructible-complexes], part 2.

Apply the projection formula of
[proposition-proper-direct-image-constructible-complexes], part 3, to $r$
and $s$. For $s$ we use the version with the pulled-back factor on the
left; it follows from the usual version by the symmetry of the tensor
product and its compatibility with pullback. The composition
isomorphisms for pullback respect the tensor products and the transported
counits. Consequently, taking adjoint transposes through
$q^*\simeq r^*s^*$ expresses the Künneth map as a composite of these base
change and projection formula isomorphisms, together with the composition
isomorphism for direct image. Its transpose is precisely the tensor
product of the two transported counits, so this composite is the stated
Künneth map.
