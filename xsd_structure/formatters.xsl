<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:extu="rebelrunner_unformatted.xsd" 
    xmlns:ext="rebelrunner.xsd" 
    xmlns="skeleton.xsd" 
    >
    <xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes"/>

    <xsl:template match="@*|*">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="extu:posts">
        <posts>
            <xsl:apply-templates select="@*|*"/>
        </posts>
    </xsl:template>

    <xsl:template match="extu:posts/@source_url">
        <xsl:attribute name="source">popular</xsl:attribute>
    </xsl:template>
</xsl:stylesheet>
