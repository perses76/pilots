<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:n="base.xml">
   <xsl:import href="base.xslt"/>

   <xsl:template match="n:hello_world">
        <xsl:apply-imports/> 
        <text> - extension</text>
    </xsl:template>

</xsl:stylesheet>
