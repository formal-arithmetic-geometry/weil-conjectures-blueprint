+++
kind = "proof"
of = "corollary-serre-duality-field-extension--1"
order = 1527005
uses = []
+++
For a separated $X$, choose a finite affine open cover. Its intersections
are affine, and the Čech complex computes quasi-coherent cohomology.
The affine pullback formula identifies the complex after base change
with its tensor product by $k'$. Tensoring over $k$ is exact, so the
canonical base change map is an isomorphism in every degree.

For a quasi-separated $X$, argue by induction on compact open subsets,
adding an affine open $V$ to a compact open $U$. The intersection
$U\cap V$ is quasi-compact by quasi-separatedness and is separated
because it is an open subscheme of $V$. Apply the separated case to
$V$ and $U\cap V$, the induction
hypothesis to $U$, and the Mayer–Vietoris sequences to obtain the
comparison on $U\cup V$. Inverting this comparison gives the displayed
isomorphism. The equality of finite ranks follows from invariance of
finite rank under extension of scalars.
