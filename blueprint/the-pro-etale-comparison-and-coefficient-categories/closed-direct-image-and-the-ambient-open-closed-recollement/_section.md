+++
id = "closed-direct-image-and-the-ambient-open-closed-recollement"
kind = "section"
title = "Closed direct image and the ambient open-closed recollement"
order = 2735
+++
The presheaf formula of the previous section is turned into the recollement
package for a closed immersion $i:Z\hookrightarrow X$ on the *ambient*
pro-etale site, with no constructibility hypothesis anywhere. Closed
operations localise along weakly etale maps
[lem-exc-closed-localization], which reduces every statement to an affine
base; there the formula makes the counit $i^*i_*G\to G$ an isomorphism, so
$i_*$ is fully faithful [lem-exc-proetale-closed-fully-faithful]. Lifting a
covering of the closed fibre and filling in the quasi-compact complement
[lem-exc-closed-cover-extension] gives exactness of $i_*$
[lem-exc-proetale-closed-exact] and the detection statement
[lem-exc-open-closed-detection]; together they identify the essential image
of $i_*$ as the sheaves killed by $j^*$
[lem-exc-proetale-closed-essential-image]. On the open side $j^*j_!=\operatorname{id}$
[lem-exc-proetale-open-unit] and $i^*j_!=0$
[lem-exc-closed-restriction-extension-zero], and the two sides assemble into
the short exact sequence [thm-exc-proetale-open-closed-exact], its derived
triangle [thm-exc-proetale-recollement], and the two recollement adjunctions
[prop-weil-open-closed-recollement-adjunctions].

The last proposition is stated in the master interface; it is proved here so
that the geometric closed-site input precedes it.
