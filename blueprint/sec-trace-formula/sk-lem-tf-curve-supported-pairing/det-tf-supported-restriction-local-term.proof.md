+++
kind = "proof"
of = "det-tf-supported-restriction-local-term"
uses = ["det-tf-supported-restriction", "def-trf-local-term", "lem-trf-trace-map-from-external-duality", "lem-trf-trace-class-diagonal-pairing"]
+++
By [det-tf-supported-restriction], $v$ corresponds to $[v]$ under exceptional adjunction
for $a$. The map $P\to Rb_*\omega_X$ adjoint to $\mathrm{ev}_K:b^*P\to\omega_X$ is the map
used to define the trace morphism of [lem-trf-trace-map-from-external-duality]. Hence
$\mathrm{ev}_K\circ\rho_{a,b}$ and the trace-class construction of [def-trf-local-term] are
both adjoint to the same composite

$$
 Ra_*a^!P\longrightarrow P\longrightarrow Rb_*\omega_X .
$$

Exceptional proper base change for $b$ identifies the supported adjoint of this composite
with the defining trace map $a^!P\to Ri_*\omega_y$, $i:\{y\}\hookrightarrow X$; the
triangle identities of the ordinary and exceptional adjunctions then give equality of the
two classes in $H^0(y,\omega_y)$, including the evaluation normalization and the Koszul
symmetry. This is the diagonal form of the trace class, [lem-trf-trace-class-diagonal-pairing],
after interchanging the two product factors. Applying $\int_y$ gives
$\operatorname{LT}_y(v)$. The constructions may be carried out on constructible étale
models, restriction to $T$ being the filtered limit over étale neighbourhoods of $(y,y)$;
the comparison theorems identify inverse images, exceptional adjunctions, duality and
support maps with their proétale counterparts.
